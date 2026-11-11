"""Shared helpers for the curated Pepys network: schema, IO, and identifier rules.

Stdlib only, so validate.py runs anywhere. Only the .xlsx round-trip scripts
need openpyxl.
"""
import csv
import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CURATED = os.path.join(REPO, "network-data", "curated")
NODES = os.path.join(CURATED, "nodes.csv")

NODE_COLS = ["id", "name", "variants", "location", "latitude", "longitude",
             "notes", "evidence"]
# notes  -- locational and curatorial gloss; supports the GRA's coordinate work
# evidence -- the diary passage that warrants the identification
# variants -- the diary's other spellings for this same place, "; "-separated
EDGE_COLS = ["id", "source", "target", "year", "month", "day", "mode",
             "named_companions", "notes", "evidence"]
# Edges carry the same split as nodes: evidence is Claude's warrant for the
# leg, quoted from the diary; notes is the GRA's column and Claude does not
# write in it. named_companions was "companions" until 12 Nov 2026.

# Controlled vocabulary for edge.mode. Extend deliberately, not ad hoc.
MODES = {"walk", "coach", "boat", "horse", "wagon", "sedan", "cart", "ship"}

# README principle 4: unknown locations are <type>_unknown_<n>. The GRA's May
# 1660 review also introduced a place-qualified form (cliff_unknown_deal,
# dutch_ship_unknown), so both are accepted; validate.py warns on the second
# because principle 4 as written still asks for a number. See HUMANDECISIONS
# section A2.
UNKNOWN_NUM_RE = re.compile(r"^[a-z][a-z_]*_unknown_\d+$")
UNKNOWN_WORD_RE = re.compile(r"^[a-z][a-z_]*_unknown(_[a-z]+)?$")
UNKNOWN_RE = UNKNOWN_NUM_RE  # kept for callers wanting the strict form
ID_RE = re.compile(r"^[a-z0-9]+(_[a-z0-9]+)*$")

# Old Style: the year began 25 March, so 1 Jan - 24 Mar carries a split year.
OLD_STYLE_RE = re.compile(r"^\d{4}/\d{2}$")


def edges_path(year):
    return os.path.join(CURATED, "edges_%s.csv" % year)


def edge_years():
    out = []
    if os.path.isdir(CURATED):
        for fn in sorted(os.listdir(CURATED)):
            m = re.match(r"^edges_(\d{4})\.csv$", fn)
            if m:
                out.append(m.group(1))
    return out


def read_csv(path, cols):
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    for i, r in enumerate(rows):
        missing = [c for c in cols if c not in r]
        if missing:
            raise SystemExit("%s row %d missing columns: %s"
                             % (path, i + 2, ", ".join(missing)))
    return rows


def write_csv(path, cols, rows):
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({c: (r.get(c) or "") for c in cols})


def read_nodes():
    return read_csv(NODES, NODE_COLS)


def read_edges(year):
    return read_csv(edges_path(year), EDGE_COLS)


def all_edges():
    """Every edge across every year file, tagged with its source file."""
    out = []
    for y in edge_years():
        for r in read_edges(y):
            r = dict(r)
            r["_year_file"] = y
            out.append(r)
    return out


def companion_list(raw):
    """Edge named_companions is a single '; '-separated field."""
    return [p.strip() for p in (raw or "").split(";") if p.strip()]


def next_edge_id(existing):
    """The next free edge id in the 1xxxxx block.

    Ids are CONTIGUOUS in row order from 100001, so inserting or removing a leg
    mid-month means renumbering everything after it. Never cite an id where the
    reference has to last -- cite a date and a leg. See HUMANDECISIONS.md.
    """
    nums = [int(e["id"]) for e in existing if str(e.get("id", "")).isdigit()]
    return max(nums) + 1 if nums else 100001


def variant_list(raw):
    """Node variants are a single '; '-separated field, like companions."""
    return [p.strip() for p in (raw or "").split(";") if p.strip()]
