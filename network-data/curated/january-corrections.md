# Corrections applied to January 1659/60 during migration

The curated January data was migrated from `node-list.xlsx` / `edge-list.xlsx`
unchanged, then `scripts/validate.py` reported 77 errors. These are the fixes,
recorded here because they were applied in the same commit as the migration
and so are not visible as a git diff. **Please spot-check them.**

After: 77 nodes, 294 edges, 0 validation errors.

## 1. Identifier drift between the two sheets (53 edge endpoints)

The edge list referred to places by a slightly different id than the node list
used, so these edges pointed at nothing. Renamed the edge endpoints to the
canonical node id in every case — no node ids were changed:

| in edge list | canonical node id | edges affected |
|---|---|---|
| `wills_ale_house` | `wills_alehouse` | 28 |
| `george_downings_lodging` | `george_downings_lodgings` | 15 |
| `mr_mossum_church` | `robert_mossum_church` | 4 |
| `mother_lams` | `mother_lams_pub` | 2 |
| `the_half_moon` | `the_half_moon_alehouse` | 2 |
| `william_fuller_lodgings` | `william_fuller_lodging` | 1 |
| `tower_of_menagerie` | `tower_menagerie` | 1 |

These also caused 17 of the 18 continuity breaks: an edge arriving at
`george_downings_lodging` followed by one departing `george_downings_lodgings`
read as a gap in the walk.

## 2. Two places referenced by edges but missing from the node list

Added, with identifications from the entries that mention them:

- **`the_sun_pub`** — The Sun Tavern, Chancery Lane. Used by edges on 20 and
  23 January. "I met with Mr. Woodfine and drank with him at the Sun in
  Chancery Lane" (20 Jan). Coordinates left blank.
- **`richard_sherwin_office`** — Used by edges on 27 January. "he sent me to
  Mr. Sherwin's about getting Mr. Squib to come to him tomorrow" (27 Jan).
  Location and coordinates left blank — the address is not given.

## 3. One missing trip — 13 January (new edge `100294`)

The only substantive addition. Edge `100116` arrived `home_axe_yard` and
`100117` departed `sandwich_lodgings`, with no leg between them. The entry
reads:

> ...and so carried her home angry. **Thence I went to Mrs. Jem**, and found
> her up and merry...

Added `home_axe_yard → sandwich_lodgings`, walk, no companions. Network4 reads
this day the same way. Given the next id in sequence (`100294`) and placed in
the correct row position, per the id rule in `DECISIONS.md`.

## 4. One companion casing inconsistency

"Clerk of Sandwich troop" → "Clerk of Sandwich Troop" on one edge, to match the
15 other occurrences.

## Not changed

The validator's remaining 8 warnings were left alone, as they need a curatorial
decision rather than a fix. They are listed as open questions in `DECISIONS.md`
— chiefly whether `peter_gunning_church` and `exeter_house_chapel` are the same
place, and the `name` fields that read "Father House" and "Mr Crews House".
