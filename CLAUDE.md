# Networking Pepys — working notes for Claude

A spatial network of *The Diary of Samuel Pepys* (1660–1669). Nodes are places;
directed edges are trips between them. Being reconstructed month by month:
Claude drafts, the project GRA reviews, rulings are written down.

## Before drafting anything

1. Read `DECISIONS.md` — the rulings already made. Apply them; do not
   re-litigate them. If a case isn't covered, draft the most defensible reading
   and **flag it** for the team rather than deciding silently.
2. Read `README.md` principles 1–12 for identifier naming.
3. Check `network-data/curated/nodes.csv` for an existing node before inventing
   one. Variant spellings and honorific differences are the main source of
   accidental duplicates.

## Canonical data

`network-data/curated/*.csv` is the source of truth. The `.xlsx` files at the
repo root are a generated view for the GRA to edit — never hand-edit a CSV to
reflect a workbook change, run `scripts/from_xlsx.py`.

Do not modify `network-data/first-gen-Claude-networks/` (archived 2026
experiments) or `years/*.txt` (the source text).

## Never hand over a chunk that fails validation

```sh
python3 scripts/validate.py --year <year> --month <month>
```

Zero ERRORs is the bar. Fix them before reporting the chunk as drafted.

## Scripts

| | |
|---|---|
| `scripts/validate.py` | schema, references, continuity, dates, conventions |
| `scripts/worksheet.py` | review worksheet: diary entry beside drafted edges |
| `scripts/diff_firstgen.py` | cross-check against the 2026 first-gen networks |
| `scripts/to_xlsx.py` / `from_xlsx.py` | lossless CSV ↔ Excel round-trip |
| `scripts/pepys.py` / `diary.py` | shared schema helpers / diary text splitter |

Stdlib only, except the two `.xlsx` scripts, which need `openpyxl`.

## Conventions that are easy to get wrong

- **Old Style years.** 1 Jan – 24 Mar is `1659/60`; from 25 Mar it is `1660`.
- **Continuity.** Every departure leaves the previous arrival, across day
  boundaries too. If a day cannot be closed, the night was spent elsewhere —
  model it, don't paper over it.
- **Edge ids never get renumbered.** Insert at the right row with the next free
  id.
- **Companions** travel *with* Pepys; people met at the destination do not count.
- **Never invent coordinates.** That field is the GRA's.
- Full detail in `WORKFLOW.md`.
