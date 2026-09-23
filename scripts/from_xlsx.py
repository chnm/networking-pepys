#!/usr/bin/env python3
"""Import node-list.xlsx / edge-list.xlsx into the canonical CSVs.

    python3 scripts/from_xlsx.py                    # both workbooks
    python3 scripts/from_xlsx.py --nodes-only
    python3 scripts/from_xlsx.py --edges-only --year 1660

Edge rows are routed to network-data/curated/edges_<year>.csv. Old Style years
("1659/60") are filed under the calendar year they fall in -- 1659/60 is
January-March 1660, so it lives in edges_1660.csv with the year string intact.
"""
import argparse
import collections
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pepys

try:
    from openpyxl import load_workbook
except ImportError:
    raise SystemExit("needs openpyxl:  pip install openpyxl")


def fmt(v):
    """Render a cell as text without float noise (51.502912000000002 -> 51.502912)."""
    if v is None:
        return ""
    if isinstance(v, float):
        s = repr(round(v, 9))
        return s.rstrip("0").rstrip(".") if "." in s else s
    return str(v).strip()


def read_sheet(path, cols):
    ws = load_workbook(path, data_only=True).worksheets[0]
    rows = list(ws.iter_rows(values_only=True))
    if not rows:
        raise SystemExit("%s: empty sheet" % path)
    header = [fmt(c).lower() for c in rows[0]]
    missing = [c for c in cols if c not in header]
    if missing:
        raise SystemExit("%s: header is missing %s (found: %s)"
                         % (path, ", ".join(missing), ", ".join(header)))
    idx = {c: header.index(c) for c in cols}
    out = []
    for raw in rows[1:]:
        rec = {c: fmt(raw[idx[c]]) if idx[c] < len(raw) else "" for c in cols}
        if any(rec.values()):
            out.append(rec)
    return out


def calendar_year(year_field):
    """'1659/60' -> 1660; '1663' -> 1663."""
    y = year_field.strip()
    if pepys.OLD_STYLE_RE.match(y):
        head, tail = y.split("/")
        return int(head[:2] + tail)
    if re.match(r"^\d{4}$", y):
        return int(y)
    raise SystemExit("unparseable year %r -- expected 1663 or 1662/63" % year_field)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nodes-xlsx", default=os.path.join(pepys.REPO, "node-list.xlsx"))
    ap.add_argument("--edges-xlsx", default=os.path.join(pepys.REPO, "edge-list.xlsx"))
    ap.add_argument("--nodes-only", action="store_true")
    ap.add_argument("--edges-only", action="store_true")
    args = ap.parse_args()

    os.makedirs(pepys.CURATED, exist_ok=True)

    if not args.edges_only:
        nodes = read_sheet(args.nodes_xlsx, pepys.NODE_COLS)
        pepys.write_csv(pepys.NODES, pepys.NODE_COLS, nodes)
        print("nodes.csv        %4d rows" % len(nodes))

    if not args.nodes_only:
        edges = read_sheet(args.edges_xlsx, pepys.EDGE_COLS)
        by_year = collections.defaultdict(list)
        for e in edges:
            by_year[calendar_year(e["year"])].append(e)
        for year in sorted(by_year):
            pepys.write_csv(pepys.edges_path(year), pepys.EDGE_COLS, by_year[year])
            print("edges_%s.csv   %4d rows" % (year, len(by_year[year])))


if __name__ == "__main__":
    main()
