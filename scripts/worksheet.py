#!/usr/bin/env python3
"""Build a review worksheet: each day's diary entry beside its drafted edges.

    python3 scripts/worksheet.py --year 1660 --month 2 --days 1-15

The point is that you never have to open the diary in a second window. For each
day you get the entry text, then the edges drafted from it in order, then any
node introduced that day. Check the sequence against the prose, mark the day,
move on.
"""
import argparse
import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import diary
import pepys


def parse_days(spec):
    if not spec:
        return None
    out = set()
    for part in spec.split(","):
        if "-" in part:
            a, b = part.split("-")
            out.update(range(int(a), int(b) + 1))
        else:
            out.add(int(part))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--year", required=True)
    ap.add_argument("--month", type=int, required=True)
    ap.add_argument("--days", help="e.g. 1-15 or 3,7,9")
    ap.add_argument("--out", help="write here instead of stdout")
    args = ap.parse_args()

    days = parse_days(args.days)
    nodes = {n["id"]: n for n in pepys.read_nodes()}
    year_edges = pepys.read_edges(args.year)
    edges = [e for e in year_edges if e["month"].strip() == str(args.month)]
    if not edges:
        raise SystemExit("no edges drafted for %s-%02d" % (args.year, args.month))
    by_day = collections.defaultdict(list)
    for e in edges:
        by_day[int(e["day"])].append(e)

    # "New" means new to the whole dataset, not merely first seen this month,
    # so places carried over from earlier chunks are not re-listed.
    seen_before = set()
    for e in pepys.all_edges():
        if (e["_year_file"], e["month"].strip()) == (args.year, str(args.month)):
            continue
        if (e["_year_file"] < args.year
                or (e["_year_file"] == args.year
                    and int(e["month"]) < args.month)):
            seen_before.add(e["source"].strip())
            seen_before.add(e["target"].strip())

    entries = diary.entries(args.year, args.month)
    month_name = diary.MONTHS[args.month - 1].title()
    # Use the year exactly as the edges record it, Old Style included.
    year_label = edges[0]["year"].strip() or args.year

    # A node counts as "new" on the first day an edge touches it this month,
    # provided no earlier chunk used it.
    first_seen = {}
    for d in sorted(by_day):
        for e in by_day[d]:
            for end in ("source", "target"):
                ref = e[end].strip()
                if ref not in seen_before:
                    first_seen.setdefault(ref, d)

    L = []
    L.append("# Review worksheet - %s %s" % (month_name, year_label))
    L.append("")
    L.append("%d edges over %d days. Mark each day `OK`, `FIX: ...`, or "
             "`FLAG: ...` (a FLAG becomes a rule in DECISIONS.md)." %
             (len(edges), len(by_day)))
    L.append("")

    for (mon, day) in sorted(entries):
        if days and day not in days:
            continue
        L.append("---")
        L.append("")
        L.append("## %d %s %s" % (day, month_name, year_label))
        L.append("")
        L.append("**Verdict:** _______")
        L.append("")
        for para in diary.flow(entries[(mon, day)]):
            L.append("> %s" % para)
            L.append(">")
        L.append("")

        seq = by_day.get(day, [])
        if not seq:
            L.append("_No movement drafted for this day._")
            L.append("")
            continue

        L.append("| # | from | to | mode | companions | notes |")
        L.append("|---|------|----|------|------------|-------|")
        for e in seq:
            L.append("| %s | %s | %s | %s | %s | %s |"
                     % (e["id"], e["source"], e["target"], e["mode"],
                        e["companions"].replace("|", "/"),
                        e["notes"].replace("|", "/")))
        L.append("")

        fresh = [nid for nid, d in first_seen.items() if d == day]
        if fresh:
            L.append("**New places:**")
            L.append("")
            for nid in sorted(fresh):
                n = nodes.get(nid)
                if n:
                    bits = [b for b in (n["name"], n["location"], n["notes"]) if b]
                    L.append("- `%s` - %s" % (nid, " / ".join(bits)))
                else:
                    L.append("- `%s` - **MISSING from nodes.csv**" % nid)
            L.append("")

    text = "\n".join(L) + "\n"
    if args.out:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text)
        print("wrote %s (%d days)" % (args.out, len(by_day) if not days else
                                      len(days & set(by_day))))
    else:
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
