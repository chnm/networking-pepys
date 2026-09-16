#!/usr/bin/env python3
"""Validate the curated Pepys network. Stdlib only.

    python3 scripts/validate.py                 # everything
    python3 scripts/validate.py --year 1660
    python3 scripts/validate.py --year 1660 --month 2

ERRORs are defects (broken references, continuity gaps, bad dates) and set a
non-zero exit code. WARNs are things to eyeball -- near-duplicate identifiers,
missing coordinates -- and never fail the run.

No draft should ever be handed over with an ERROR outstanding.
"""
import argparse
import calendar
import collections
import difflib
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pepys

errors, warnings = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def collapse(s):
    """Fold harder than norm(): drop word boundaries too, so
    'wills_ale_house' and 'wills_alehouse' collide."""
    return norm(s).replace(" ", "")


def suggest(ref, candidates):
    """Best guess at the node a broken reference meant."""
    exact = [c for c in candidates if collapse(c) == collapse(ref)]
    if exact:
        return exact[0]
    contained = sorted((c for c in candidates
                        if collapse(ref) in collapse(c)
                        or collapse(c) in collapse(ref)), key=len)
    if contained:
        return contained[0]
    close = difflib.get_close_matches(ref, candidates, n=1, cutoff=0.8)
    return close[0] if close else None


def norm(s):
    """Fold an identifier/name for near-duplicate detection.

    Strips punctuation and case, drops a trailing plural 's' on each word, so
    'george_downings_lodging' and 'George Downings Lodgings' collide.
    """
    words = re.split(r"[^a-z0-9]+", (s or "").lower().replace("'", "")
                                                   .replace("\u2019", ""))
    return " ".join(w[:-1] if len(w) > 3 and w.endswith("s") else w
                    for w in words if w)


# --------------------------------------------------------------- nodes
def check_nodes(nodes):
    seen = {}
    by_norm = collections.defaultdict(list)
    unknown_nums = collections.defaultdict(list)

    for i, n in enumerate(nodes):
        line = i + 2
        nid = n["id"].strip()
        if not nid:
            err("nodes.csv:%d  blank id" % line)
            continue
        if nid in seen:
            err("nodes.csv:%d  duplicate id %r (first seen line %d)"
                % (line, nid, seen[nid]))
        seen[nid] = line

        if not pepys.ID_RE.match(nid):
            err("nodes.csv:%d  id %r breaks the naming rules "
                "(lowercase a-z0-9, single underscores between words)" % (line, nid))
        if not n["name"].strip():
            err("nodes.csv:%d  node %r has no name" % (line, nid))

        if "_unknown" in nid:
            if not pepys.UNKNOWN_RE.match(nid):
                err("nodes.csv:%d  %r must be <type>_unknown_<n> "
                    "(README principle 4)" % (line, nid))
            else:
                kind, num = nid.rsplit("_unknown_", 1)
                unknown_nums[kind].append((int(num), line, nid))

        by_norm[norm(nid)].append((nid, line))

        lat, lon = n["latitude"].strip(), n["longitude"].strip()
        if bool(lat) != bool(lon):
            err("nodes.csv:%d  node %r has only one of latitude/longitude"
                % (line, nid))
        for label, raw, lo, hi in (("latitude", lat, 49.0, 60.0),
                                   ("longitude", lon, -11.0, 12.0)):
            if raw:
                try:
                    v = float(raw)
                except ValueError:
                    err("nodes.csv:%d  node %r has non-numeric %s %r"
                        % (line, nid, label, raw))
                else:
                    if not lo <= v <= hi:
                        err("nodes.csv:%d  node %r %s %s is outside the "
                            "England/Low Countries range" % (line, nid, label, raw))

    for kind, entries in sorted(unknown_nums.items()):
        nums = sorted(e[0] for e in entries)
        expected = list(range(1, len(nums) + 1))
        if nums != expected:
            warn("%s_unknown_* is numbered %s -- expected %s (gaps or repeats)"
                 % (kind, nums, expected))

    for key, group in sorted(by_norm.items()):
        if len(group) > 1:
            warn("near-duplicate node ids -- same place twice? %s"
                 % ", ".join("%s (line %d)" % g for g in group))

    # An id that has drifted away from its own name is the usual sign of a typo.
    for i, n in enumerate(nodes):
        nid, name = n["id"].strip(), n["name"].strip()
        if nid and name:
            a, b = collapse(nid), collapse(name)
            if a != b and a not in b and b not in a:
                warn("nodes.csv:%d  id %r and name %r do not correspond"
                     % (i + 2, nid, name))
    return seen


# --------------------------------------------------------------- edges
def check_dates(edges):
    """Old Style: the legal year began 25 March, so 1 Jan - 24 Mar is split."""
    for e in edges:
        where = "edges_%s.csv id=%s" % (e["_year_file"], e["id"])
        try:
            month, day = int(e["month"]), int(e["day"])
        except ValueError:
            err("%s  non-numeric month/day (%r/%r)" % (where, e["month"], e["day"]))
            continue
        if not 1 <= month <= 12:
            err("%s  month %d out of range" % (where, month))
            continue

        cal = int(e["_calendar_year"])
        if not 1 <= day <= calendar.monthrange(cal, month)[1]:
            err("%s  day %d invalid for month %d of %d" % (where, day, month, cal))

        split = month < 3 or (month == 3 and day <= 24)
        y = e["year"].strip()
        if split:
            if not pepys.OLD_STYLE_RE.match(y):
                err("%s  %d-%02d-%02d falls before 25 March, so year should be "
                    "Old Style %d/%02d, not %r"
                    % (where, cal, month, day, cal - 1, cal % 100, y))
        elif not re.match(r"^\d{4}$", y):
            err("%s  %d-%02d-%02d falls on/after 25 March, so year should be "
                "plain %d, not %r" % (where, cal, month, day, cal, y))


def check_edges(edges, node_ids):
    seen = {}
    for e in edges:
        where = "edges_%s.csv id=%s" % (e["_year_file"], e["id"])
        eid = e["id"].strip()
        if not eid.isdigit():
            err("%s  id must be numeric" % where)
        elif eid in seen:
            err("%s  duplicate edge id (also in edges_%s.csv)" % (where, seen[eid]))
        else:
            seen[eid] = e["_year_file"]

        for end in ("source", "target"):
            ref = e[end].strip()
            if not ref:
                err("%s  blank %s" % (where, end))
            elif ref not in node_ids:
                near = suggest(ref, list(node_ids))
                hint = (" -- did you mean %r?" % near) if near else ""
                err("%s  %s %r is not in nodes.csv%s" % (where, end, ref, hint))

        if e["source"].strip() and e["source"].strip() == e["target"].strip():
            err("%s  self-loop on %r" % (where, e["source"]))

        mode = e["mode"].strip()
        if not mode:
            err("%s  blank mode (use 'walk' where the diary gives none)" % where)
        elif mode not in pepys.MODES:
            err("%s  mode %r is not in the controlled vocabulary (%s)"
                % (where, mode, ", ".join(sorted(pepys.MODES))))

        raw = e["companions"]
        if "," in raw and ";" not in raw:
            warn("%s  companions %r uses a comma -- separator is '; '" % (where, raw))
        for person in pepys.companion_list(raw):
            if person != person.strip(" .;"):
                warn("%s  companion %r has stray punctuation" % (where, person))


def check_continuity(edges):
    """Travel is unbroken: each departure leaves where the last arrival landed.

    Checked within a day and across consecutive diary days, so an overnight
    away from home has to be modelled explicitly rather than assumed.
    """
    days = collections.OrderedDict()
    for e in edges:
        key = (int(e["_calendar_year"]), int(e["month"]), int(e["day"]))
        days.setdefault(key, []).append(e)

    for key, seq in days.items():
        stamp = "%d-%02d-%02d" % key
        for a, b in zip(seq, seq[1:]):
            if a["target"].strip() != b["source"].strip():
                err("continuity %s: edge %s arrives %r but edge %s departs %r"
                    % (stamp, a["id"], a["target"], b["id"], b["source"]))

    keys = list(days)
    for prev, nxt in zip(keys, keys[1:]):
        end = days[prev][-1]["target"].strip()
        start = days[nxt][0]["source"].strip()
        if end != start:
            err("continuity %d-%02d-%02d -> %d-%02d-%02d: day ends at %r but the "
                "next day departs %r (add the missing leg, or check where he "
                "spent the night)" % (prev + nxt + (end, start)))

    for prev, nxt in zip(keys, keys[1:]):
        if nxt <= prev:
            err("edge rows are out of chronological order: %d-%02d-%02d appears "
                "after %d-%02d-%02d" % (nxt + prev))


def check_people(edges):
    by_norm = collections.defaultdict(set)
    for e in edges:
        for person in pepys.companion_list(e["companions"]):
            by_norm[norm(person)].add(person)
    for key, spellings in sorted(by_norm.items()):
        if len(spellings) > 1:
            warn("companion spelled %d ways: %s"
                 % (len(spellings), " | ".join(sorted(spellings))))


def check_coverage(edges, nodes, node_ids):
    used = {e[end].strip() for e in edges for end in ("source", "target")}
    for nid in sorted(set(node_ids) - used):
        warn("node %r is never used by an edge" % nid)
    missing_coords = [n["id"] for n in nodes if not n["latitude"].strip()]
    if missing_coords:
        warn("%d of %d nodes have no coordinates (human task)"
             % (len(missing_coords), len(nodes)))


# --------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--year", help="restrict to one calendar year, e.g. 1660")
    ap.add_argument("--month", type=int, help="restrict to one month (needs --year)")
    ap.add_argument("--quiet", action="store_true", help="errors only")
    args = ap.parse_args()

    nodes = pepys.read_nodes()
    if not nodes:
        raise SystemExit("no %s -- run scripts/from_xlsx.py first" % pepys.NODES)
    node_ids = check_nodes(nodes)

    years = [args.year] if args.year else pepys.edge_years()
    edges = []
    for y in years:
        rows = pepys.read_edges(y)
        if not rows and args.year:
            raise SystemExit("no edges for %s (%s)" % (y, pepys.edges_path(y)))
        for r in rows:
            r["_year_file"] = y
            r["_calendar_year"] = y
        edges.extend(rows)
    if args.month:
        edges = [e for e in edges if e["month"].strip() == str(args.month)]

    check_dates(edges)
    check_edges(edges, node_ids)
    check_continuity(edges)
    check_people(edges)
    if not args.year:
        check_coverage(edges, nodes, node_ids)

    scope = "all years" if not args.year else "%s%s" % (
        args.year, " month %d" % args.month if args.month else "")
    print("checked %d nodes, %d edges (%s)" % (len(nodes), len(edges), scope))
    if not args.quiet:
        for w in warnings:
            print("  WARN  %s" % w)
    for e in errors:
        print("  ERROR %s" % e)
    print("%d error(s), %d warning(s)" % (len(errors), len(warnings)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
