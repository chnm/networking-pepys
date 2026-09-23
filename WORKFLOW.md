# Reconstruction workflow

Claude drafts a chunk, machine checks catch the mechanical errors, you review
the history, and every ruling you make becomes a written rule. Repeat to
May 1669.

## Setup (once)

```sh
pip install openpyxl          # only needed for the .xlsx round-trip
```

## Where the data lives

`network-data/curated/` holds the canonical data as CSV, so git can diff it and
you can see exactly what changed in a review:

```
network-data/curated/
  nodes.csv          cumulative, all months   (id,name,location,latitude,longitude,notes)
  edges_1660.csv     one file per calendar year (id,source,target,year,month,day,mode,companions,notes)
  crosswalk.csv      first-gen ids -> curated ids, for the cross-check
```

You still work in Excel. The workbooks at the repo root are a **view**:

```sh
python3 scripts/to_xlsx.py                     # CSV  -> node-list.xlsx / edge-list.xlsx
python3 scripts/to_xlsx.py --year 1660 --month 2   # just one month, to review
python3 scripts/from_xlsx.py                   # your edits -> CSV
```

The round-trip is lossless: export then re-import leaves the CSVs byte-identical.
Edit the workbooks, run `from_xlsx.py`, commit the CSV diff.

## The per-chunk loop

**1. Claude drafts.** Reads the diary text for the chunk, appends edges to the
year file and new places to `nodes.csv`. Reads `DECISIONS.md` first, so
established rulings are applied rather than re-litigated.

**2. Machine checks run — before you see anything.**

```sh
python3 scripts/validate.py --year 1660 --month 2
```

ERRORs are defects and block the handoff; WARNs are for your eye. It checks:

- every edge endpoint exists in `nodes.csv` (catches id drift, with a "did you
  mean" suggestion)
- continuity within a day and across consecutive days
- Old Style year formatting, valid dates, chronological row order
- `mode` against the controlled vocabulary; duplicate and self-looping edges
- identifier conventions, `_unknown_<n>` numbering, coordinate sanity
- near-duplicate node ids and companion names spelled more than one way

No chunk is handed over with an ERROR outstanding.

**3. Cross-check against the first-generation networks.** A second opinion on
the same entries — network4 for 1660, network2 elsewhere.

```sh
python3 scripts/diff_firstgen.py --year 1660 --month 2 --bootstrap
python3 scripts/diff_firstgen.py --year 1660 --month 2
```

`--bootstrap` proposes `crosswalk.csv` rows for places not yet mapped and marks
the uncertain ones `REVIEW` — check those before trusting the output. The diff
then reports only days where the two readings disagree: a place one side visits
and the other doesn't, or an edge count that differs by more than one. Those are
the days worth re-reading.

**4. You review.** One worksheet, no second window:

```sh
python3 scripts/worksheet.py --year 1660 --month 2 --days 1-15 --out review/1660-02.md
```

Each day gives you the diary entry, the edges drafted from it in order, and any
new place introduced. Mark each day:

- `OK`
- `FIX: ...` — you correct it in the workbook
- `FLAG: ...` — ambiguous, needs a ruling

**5. Rulings become rules.** Every `FLAG` is resolved into a line in
`DECISIONS.md`, with the entry that prompted it. This is the step that makes 120
months tractable: it stops the same question recurring and stops Claude
inventing `mr_crews_house` in month 40 when `john_crews_house` was settled in
month 1.

**6. Commit.** One commit per chunk, CSV diffs reviewable line by line.

## Chunk size

Half-months to start, while the conventions are being calibrated, moving to
whole months once your corrections taper off, and quarters if they nearly stop.
January is the yardstick: 294 edges, 77 places, 30 days.

## Division of labour

| | Claude | You |
|---|---|---|
| Draft edges and new nodes | ✓ | |
| `notes` field | drafts | verifies |
| `latitude` / `longitude` | leaves blank | fills |
| Place identifications | applies `DECISIONS.md` | rules on anything new |
| Machine checks | runs before handoff | |
| Historical judgement | flags, never decides | decides |
