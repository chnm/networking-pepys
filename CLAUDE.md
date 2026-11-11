# Networking Pepys — working notes for Claude

A spatial network of *The Diary of Samuel Pepys* (1660–1669). Nodes are places;
directed edges are trips between them. Being reconstructed month by month:
Claude drafts, the project GRA reviews, rulings are written down.

## Before drafting anything

1. Read `HUMANDECISIONS.md` — the GRA's rulings. Apply them; do not
   re-litigate them. Section A is what is still waiting on a ruling; B to D are
   binding. If a case isn't covered, draft the most defensible reading and
   **flag it into section A** rather than deciding silently. Never write a
   ruling into that file yourself.
   Then read `CLAUDEDECISIONS.md` — your own drafting method, the defaults for
   when the diary is silent, and the corrections already made. Record new
   drafting judgement there, not in `HUMANDECISIONS.md`.
   `DECISIONS.md` is the closed record to 11 November 2026. Consult it for the
   history behind a rule; never add to it.
2. Read `README.md` for identifier naming. **Nothing is missing**: it is one
   Markdown ordered list of 13 principles, which renders 1–13. The literal
   numbers in the source read 1–5, 7–11, 13, 14, 16, because Markdown
   renumbers a list on render and ignores what is typed. This project cites
   the **source** numbers (so "principle 14" is ships), and those differ from
   what a reader of the rendered file sees from the sixth item on. Quote the
   principle's words alongside its number, and read the whole list.
3. Check `network-data/curated/nodes.csv` for an existing node before inventing
   one. Variant spellings and honorific differences are the main source of
   accidental duplicates, so search the `variants` column as well as `name` and
   `id` — that column exists to catch exactly this.

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
- **Edge ids are contiguous**, in row order from `100001`. Inserting or removing
  a leg mid-month means renumbering everything after it, so never cite an id
  where the reference has to last — cite a date and a leg.
- **Ships.** A named ship is one location however far she sails; the node is
  `the_` plus the vessel's name — `the_naseby`, `the_london`. The prefix keeps
  the ship *London* apart from `city_of_london`. Water travel is always
  `mode` = `boat`; there is no `ship` mode. No cabin or deck nodes.
- **Companions.** The edge column is `named_companions` (renamed from
  `companions`, 12 Nov 2026; nothing else about it changed). Only people who
  travelled *with* Pepys — someone met at the destination does not count.
- **Never invent coordinates.** That field is the GRA's.
- **`notes` vs `evidence` vs `variants`.** Both `nodes.csv` and
  `edges_<year>.csv` carry `notes` and `evidence`. **`notes` is the GRA's
  column in both — never write in it.** `evidence` is yours: the diary passage
  warranting the identification or the leg, quoted, with the date. `variants` holds the diary's *other spellings for the same
  place* ("the 3 Tun tavern" for `three_tuns_tavern`, "Mr Laxton's" for
  `john_layton_apothecary`), `; `-separated — not narrative fragments and not a
  restatement of the name. The validator cross-checks every node's name and id
  against it, so a variant recorded here stops that spelling becoming a second
  node.
- Full detail in `WORKFLOW.md`.
