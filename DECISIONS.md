# Decisions log

Every ruling made while reconstructing the network, so the same question is
never answered twice and the conventions do not drift over 120 months.

**How to use it:** when a review turns up an ambiguity, write the ruling here
and cite the entry that prompted it. Claude reads this file before drafting a
new chunk. If a rule is not written down, assume it will be broken.

Identifier naming principles live in `README.md` (principles 1-12) and are not
repeated here. This file records what those principles resolved to in practice.

---

## 1. Schema and mechanics

| Rule | Detail |
|---|---|
| **Old Style years** | The legal year began 25 March, so 1 Jan - 24 Mar carries a split year: `1659/60`. From 25 March it is a plain `1660`. Enforced by `scripts/validate.py`. |
| **Edge `id`** | A stable surrogate key in the `1xxxxx` block. Chronology comes from `year`/`month`/`day` plus **row order within a day**, never from the id. An edge inserted into an already-reviewed month takes the next free id and sits in the right row; ids are never renumbered, so nothing already reviewed or cited moves. |
| **One file per year** | `network-data/curated/edges_<year>.csv`, filed by calendar year. January 1659/60 lives in `edges_1660.csv` with the year string intact. |
| **Nodes are cumulative** | One `nodes.csv` for the whole project. A new month appends to it; it is never split by year. |
| **Continuity** | Travel is unbroken. Every departure leaves the node of the previous arrival, within a day *and* across consecutive diary days. A night spent away from home is modelled explicitly rather than assumed. |
| **Days with no movement** | Contribute no edges. The continuity check skips them (15 January 1659/60 is the first such day). |
| **`mode`** | Controlled vocabulary: `walk`, `coach`, `boat`, `horse`, `wagon`, `sedan`, `cart`, `ship`. `walk` is the default where the diary names no mode. `boat` covers wherries, barges and schuits. Extend the list in `scripts/pepys.py` deliberately, not ad hoc. |
| **`companions`** | `; `-separated. Only people who travelled *with* Pepys on that leg -- someone merely met at the destination is not a companion. Standardised names ("Elizabeth Pepys", not "my wife"). Role descriptors are acceptable where no name is known ("Quartermaster of Sandwich Troop", "unknown man"). |
| **`latitude` / `longitude`** | Human-filled only. Claude leaves them blank rather than guessing. |
| **`notes`** | Claude drafts these from the text (who lived there, how the place was identified, the entry that first mentions it). Factual and checkable; no speculation presented as fact. A genuine uncertainty is written with a question mark. |
| **Unknown places** | `<type>_unknown_<n>` per README principle 4, numbered sequentially per type across the whole project (not restarted each month). |

## 2. Place identifications

Ambiguous place-words change meaning through the diary. Each ruling holds until
superseded by a dated successor.

| Diary phrase | Node | Period | Basis |
|---|---|---|---|
| "home" | `home_axe_yard` | from 1 Jan 1659/60 | Axe Yard, Westminster |
| "my office", "the office" | `office_exchequer` | Jan 1659/60 - | Mr Downing's Exchequer office, Westminster Palace |
| "Mrs. Jem", "my Lord's lodgings" | `sandwich_lodgings` | from 1 Jan 1659/60 | Jemima Montagu lodged at the Earl of Sandwich's Whitehall lodgings |
| "my father's" | `john_pepys_house` | from 1 Jan 1659/60 | John Pepys Sr., tailor, Salisbury Court |
| "Mr. Calthrop's", "the Temple" | `lestrange_calthorpe_chamber` | from 2 Jan 1659/60 | Chancery Lane, Temple district |
| "Will's" | `wills_alehouse` | from 2 Jan 1659/60 | Old Palace Yard |
| "Catan" | `kate_petit_house` | 13 Jan 1659/60 | as read by the project team |
| "the Sun" | `the_sun_pub` | 20 Jan 1659/60 | "the Sun in Chancery Lane" |

### Changes expected later (do not apply early)

- **17 July 1660**: Pepys moves from Axe Yard to the Navy Office house in
  Seething Lane. "Home" becomes a new node from that date; the move itself is
  an edge.
- **From July 1660**: "my office" becomes the Navy Office, Seething Lane, kept
  as a node separate from the adjoining house. During Aug-Dec 1660 "the office"
  at Whitehall means the Privy Seal Office.
- **23 March - 8 June 1660**: the voyage. Ships are nodes and Pepys lives
  aboard; per README principle 12 a ship is one location even while moving. The
  *Naseby* is renamed *Royal Charles* on 23 May -- same node or two is an open
  question.
- **September 1666**: the Fire destroys much of the City. Places that move
  afterwards become new nodes, per the network-three prompt.

## 3. Open questions

Rulings needed from the project team. Claude should not decide these alone.

1. **`peter_gunning_church` vs `exeter_house_chapel`** -- both exist in
   `nodes.csv`. Gunning preached at Exeter House Chapel, and network4 reads
   29 January as a visit to Exeter House Chapel where the curated data has
   `peter_gunning_church`. Are these one place?
2. **`the_new_market` vs `market_unknown_1`** -- do these overlap?
3. **`city_of_london`** -- the `name` field currently holds a query
   ("Referencing the Royal Exchange?") rather than a name. Resolve, and move
   the uncertainty into `notes`.
4. **Names vs ids** -- `john_pepys_house` is named "Father House" and
   `john_crews_house` "Mr Crews House", which sits awkwardly with README
   principle 7 (use the most specific label we have). Rename the `name` fields?
5. **Coordinate granularity** -- several nodes share coordinates (e.g.
   `john_pepys_house` and `turner_house` are both Salisbury Court). Intended,
   or should they be distinguished?
6. **Companion roles** -- keep descriptors like "Clerk of Sandwich Troop" as
   companions, or only named people?
7. **Combined entries.** Two entries in the diary cover several days at once:
   July 1661 has "8th, 9th, Loth, 11th, 12th, 13th." (six days) and
   "16th, 17th, 18th, 19th." (four). The prose does not say which day each
   movement happened on. How should the edges be dated -- all on the first day
   of the span, spread by inference, or a new convention? `scripts/diary.py`
   currently attributes the text to every day it covers and
   `diary.combined_days()` reports them.
8. **October 1668.** Wheatley's text has no entries for 1-10 October 1668; it
   resumes on the 11th. Confirmed a genuine gap in the source, not a parsing
   artefact -- no edges for those days.
