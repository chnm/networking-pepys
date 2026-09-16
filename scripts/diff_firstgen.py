#!/usr/bin/env python3
"""Cross-check a curated month against the first-generation Claude networks.

    python3 scripts/diff_firstgen.py --year 1660 --month 2 --bootstrap
    python3 scripts/diff_firstgen.py --year 1660 --month 2

A second opinion, not an authority. The first-gen networks use their own
identifier vocabularies ("Mrs. Jem's Lodgings" where we say
`sandwich_lodgings`), so the comparison runs through an explicit crosswalk at
network-data/curated/crosswalk.csv rather than guessing at names.

  --bootstrap  proposes crosswalk rows for first-gen places in this month that
               aren't mapped yet, ranked by confidence, and appends the
               confident ones. Review them before trusting the diff.

Without a crosswalk entry a place is reported as unmapped rather than silently
treated as a disagreement.
"""
import argparse
import collections
import csv
import difflib
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pepys

FIRSTGEN = os.path.join(pepys.REPO, "network-data", "first-gen-Claude-networks")
CROSSWALK = os.path.join(pepys.CURATED, "crosswalk.csv")
CROSSWALK_COLS = ["network", "firstgen_id", "firstgen_name", "curated_id", "status"]

SOURCES = {
    "network4": (os.path.join(FIRSTGEN, "network4", "nodes.csv"),
                 [os.path.join(FIRSTGEN, "network4", "edges.csv")],
                 "Claude Code, 1660 only"),
    "network2": (os.path.join(FIRSTGEN, "network2", "pepys-nodes-network2.csv"),
                 [os.path.join(FIRSTGEN, "network2", "pepys-edges-network2.csv")],
                 "Claude Chat Opus, full diary"),
    "network1": (os.path.join(FIRSTGEN, "network1", "pepys_nodes-network1.csv"),
                 [os.path.join(FIRSTGEN, "network1", "pepys_edges-network1.csv")],
                 "Claude Chat Sonnet, full diary"),
}
MONTH_NAMES = {m.lower(): i for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July", "August",
     "September", "October", "November", "December"], start=1)}

# Dropped when folding names for match suggestions -- these differ purely by
# house style between the networks.
STOP = {"the", "of", "mr", "mrs", "dr", "my", "house", "lodging", "lodgings",
        "home", "at", "in", "a", "and", "sr", "jr", "cousin", "unspecified",
        "tavern", "alehouse", "inn", "pub", "s", "lord"}


def fold(s):
    body = re.sub(r"\([^)]*\)", " ", (s or "").lower().replace("'", ""))
    words = re.split(r"[^a-z0-9]+", body)
    keep = [w[:-1] if len(w) > 3 and w.endswith("s") else w
            for w in words if w and w not in STOP]
    return " ".join(keep)


def read_crosswalk():
    if not os.path.exists(CROSSWALK):
        return {}
    with open(CROSSWALK, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    return {(r["network"], r["firstgen_id"]): r for r in rows}


def write_crosswalk(mapping):
    rows = sorted(mapping.values(), key=lambda r: (r["network"], r["firstgen_id"]))
    pepys.write_csv(CROSSWALK, CROSSWALK_COLS, rows)


def load_firstgen(name, year, month):
    node_path, edge_paths, _ = SOURCES[name]
    with open(node_path, newline="", encoding="utf-8") as fh:
        names = {r["id"]: (r.get("name") or r["id"]) for r in csv.DictReader(fh)}
    found = []
    for p in edge_paths:
        if not os.path.exists(p):
            continue
        with open(p, newline="", encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                if str(r.get("year", "")).strip()[-4:] != str(year):
                    continue
                raw = str(r.get("month", "")).strip()
                mon = MONTH_NAMES.get(raw.lower())
                if mon is None:
                    mon = int(raw) if raw.isdigit() else None
                if mon != month:
                    continue
                found.append((int(r["day"]), r["source"], r["target"]))
    return names, found


def slug(s):
    """Collapse a slug-style identifier for comparison."""
    words = re.split(r"[^a-z0-9]+", (s or "").lower())
    return "".join(sorted(w[:-1] if len(w) > 3 and w.endswith("s") else w
                          for w in words if w and w not in STOP))


def propose(fg_id, fg_name, cur_nodes):
    """Best curated candidate for a first-gen place.

    Both vocabularies use the same slug convention, so the identifier is a
    far better signal than the display name (curated names are terse --
    "Father House" -- where first-gen names are descriptive). Identifiers are
    tried first, names only as a fallback.
    """
    ids = list(cur_nodes)
    if fg_id in cur_nodes:
        return [(fg_id, "id-exact")]

    by_slug = collections.defaultdict(list)
    for nid in ids:
        by_slug[slug(nid)].append(nid)
    hit = by_slug.get(slug(fg_id))
    if hit:
        return [(hit[0], "id-folded")]

    contained = sorted((nid for nid in ids
                        if slug(nid) and (slug(nid) in slug(fg_id)
                                          or slug(fg_id) in slug(nid))),
                       key=lambda nid: abs(len(slug(nid)) - len(slug(fg_id))))
    if contained:
        return [(contained[0], "id-partial")]

    close = difflib.get_close_matches(fg_id, ids, n=1, cutoff=0.72)
    if close:
        return [(close[0], "id-fuzzy")]

    names = {nid: fold(cur_nodes[nid]["name"] or nid) for nid in ids}
    target = fold(fg_name)
    if target:
        exact = [nid for nid, f in names.items() if f and f == target]
        if exact:
            return [(exact[0], "name-exact")]
        nclose = difflib.get_close_matches(target, [f for f in names.values() if f],
                                           n=1, cutoff=0.8)
        if nclose:
            nid = next(n for n, f in names.items() if f == nclose[0])
            return [(nid, "name-fuzzy")]
    return []


def sequence(day_edges):
    if not day_edges:
        return []
    return [day_edges[0][0]] + [t for _, t in day_edges]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--year", required=True)
    ap.add_argument("--month", type=int, required=True)
    ap.add_argument("--against", default=None, choices=sorted(SOURCES))
    ap.add_argument("--bootstrap", action="store_true",
                    help="propose and save crosswalk rows for unmapped places")
    args = ap.parse_args()

    name = args.against or ("network4" if args.year == "1660" else "network2")
    fg_names, fg_rows = load_firstgen(name, args.year, args.month)
    if not fg_rows:
        raise SystemExit("%s has no edges for %s-%02d" % (name, args.year, args.month))

    cur_nodes = {n["id"]: n for n in pepys.read_nodes()}
    cur_rows = [(int(e["day"]), e["source"], e["target"])
                for e in pepys.read_edges(args.year)
                if e["month"].strip() == str(args.month)]
    if not cur_rows:
        raise SystemExit("no curated edges for %s-%02d" % (args.year, args.month))

    xwalk = read_crosswalk()
    present = {p for _, s, t in fg_rows for p in (s, t)}

    if args.bootstrap:
        added = 0
        for fid in sorted(present):
            if (name, fid) in xwalk:
                continue
            guesses = propose(fid, fg_names.get(fid, fid), cur_nodes)
            cid, how = guesses[0] if guesses else ("", "unmatched")
            xwalk[(name, fid)] = {
                "network": name, "firstgen_id": fid,
                "firstgen_name": fg_names.get(fid, ""),
                "curated_id": cid,
                "status": how if cid else "REVIEW: no curated match",
            }
            added += 1
        write_crosswalk(xwalk)
        print("bootstrap: added %d crosswalk row(s) to %s"
              % (added, os.path.relpath(CROSSWALK, pepys.REPO)))
        need = [r for r in xwalk.values()
                if r["network"] == name and r["firstgen_id"] in present
                and (not r["curated_id"] or r["status"].startswith("REVIEW")
                     or r["status"].endswith("fuzzy")
                     or r["status"].endswith("partial"))]
        if need:
            print("%d row(s) need a human eye (no match, fuzzy, or partial):"
                  % len(need))
            for r in sorted(need, key=lambda r: r["firstgen_id"]):
                print("   %-28s %-42s -> %-26s %s"
                      % (r["firstgen_id"], r["firstgen_name"][:42],
                         r["curated_id"] or "(none)", r["status"]))
        print()

    def to_curated(fid):
        r = xwalk.get((name, fid))
        return (r or {}).get("curated_id") or None

    unmapped = sorted(p for p in present if not to_curated(p))
    cur, fg = collections.defaultdict(list), collections.defaultdict(list)
    for day, s, t in cur_rows:
        cur[day].append((s, t))
    for day, s, t in fg_rows:
        fg[day].append((s, t))

    print("curated  %s-%02d: %d edges over %d days"
          % (args.year, args.month, len(cur_rows), len(cur)))
    print("%-8s %s-%02d: %d edges over %d days   (%s)"
          % (name, args.year, args.month, len(fg_rows), len(fg), SOURCES[name][2]))
    if unmapped:
        print("\n%d first-gen place(s) in this month are not in the crosswalk; "
              "they are excluded from the comparison below.\n   %s"
              % (len(unmapped), ", ".join(unmapped)))
        print("   (run with --bootstrap to propose mappings)")
    print()

    findings = 0
    for day in sorted(set(cur) | set(fg)):
        cur_seq = sequence(cur.get(day, []))
        fg_seq = [to_curated(p) for p in sequence(fg.get(day, []))]
        fg_seq = [p for p in fg_seq if p]
        cur_set, fg_set = set(cur_seq), set(fg_seq)

        only_fg = [p for p in dict.fromkeys(fg_seq) if p not in cur_set]
        only_cur = [p for p in dict.fromkeys(cur_seq) if p not in fg_set
                    and any(to_curated(x) for x in sequence(fg.get(day, [])))]
        delta = abs(len(fg.get(day, [])) - len(cur.get(day, [])))

        if not only_fg and not only_cur and delta <= 1:
            continue
        findings += 1
        print("day %-2d  curated %2d edges | %s %2d edges"
              % (day, len(cur.get(day, [])), name, len(fg.get(day, []))))
        if only_fg:
            print("        only in %s -- possible omission: %s"
                  % (name, ", ".join(only_fg)))
        if only_cur:
            print("        only in curated -- confirm against the entry: %s"
                  % ", ".join(only_cur))
        print()

    print("%d day(s) worth re-reading." % findings if findings
          else "no material disagreements.")


if __name__ == "__main__":
    main()
