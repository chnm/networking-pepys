# Human decisions

**The GRA's file.** Everything here is a decision only a person can make: a
historical judgement, a curatorial convention, or a ruling on an ambiguity the
diary does not resolve. It is the complete record of those decisions from
January 1659/60 onward — questions still open in section A, rules in force in
B and C, and every decision already made, chunk by chunk, in section D.
Claude applies what it says and may add questions to section A; Claude does not
write rulings into this file.

Claude's own drafting reasoning — the defaults it applies when the text is
silent, the readings it takes, the corrections it makes to its own work — lives
in `CLAUDEDECISIONS.md`. `DECISIONS.md` is the closed historical record of
everything decided up to 11 November 2026 and is no longer added to.

**How to use it.** Section A is the queue: decisions waiting on you. Sections B
to D are what has already been settled, which Claude treats as binding. When
you answer something in A, move it into B, C or D so the next chunk picks it up.

Identifier naming principles live in `README.md`. Its source numbering and its
rendered numbering differ from the sixth principle on, so quote a principle's
words alongside its number — see `CLAUDEDECISIONS.md` for the mechanics.

---

# A. Waiting on a ruling

Nothing below is settled. Claude has drafted each on the most defensible
reading it could find and flagged it rather than deciding silently.

## A1. Carried over, still unanswered

| # | Question | Where it stands now |
|---|---|---|
| 1 | **`navy_office` and the July 1660 house** — Pepys moves into the house adjoining the Navy Office in Seething Lane on 17 July 1660. Two nodes or one? | Two, provisionally. Also bears on the Navy Commissioners of 15 June 1660, drafted as `navy_office`. **Due now — July is the next chunk.** |
| 2 | **6 March and Mrs Jem.** The review retargeted that day's leg to `sandwich_lodgings` and dropped the next, so the day no longer records the visit to her. | Sits against the ruling placing her at `scott_house` for all of 1–15 March. Flagged, not reverted. |
| 3 | **Seven companion near-misses.** `Jemima`/`Jemimah Montagu`, `John Hawley`/`Hawly`, `Mr Hawley`/`Hawly`, `Matthew Lock`/`Locke`, `Mr Shepley`/`Sheply`, `William Simons`/`Symons`, and `William Howe`/`William Howell` — the last probably two different men. | Untouched. Choosing the canonical spelling is a curatorial call, as is whether bare `Mr Hawly` forms become the full names used elsewhere. |
| 4 | **Identifications made for one day only.** "Mr Thomas" (7 edges) / "Thomas Crew" (2), named on 23 March as John Crew's son; "Mr Woodfine" (2) / "Thomas Woodfine" (1), named on 18 March. | Not propagated to other dates. Extending an identification across dates is a curatorial judgement. |
| 5 | **Kate Sterpin, 22 March.** "took leave of Kate Sterpin" gives no place. She may or may not be the Catan of `kate_petit_house`. | Unmodelled. |
| 6 | **3 April, an aborted landing.** "my Lord went on shore, and after him I and Capt. Sparling went in his boat, but ... we could not stay." | No edge. If it counts, it needs a node for an unnamed shore. |
| 7 | **Everyone else moves and Pepys does not.** Through the voyage his people travel constantly — Shipley to Sheppy, Stayner to Dover, Burr ashore — and none of it is an edge. | Correct as drafted, since the network records Pepys. Worth confirming that is intended for the voyage. |
| 8 | **`lion_tavern` and `cock_tavern` have no location.** The entries name no street. | Blank. Marked for manual check. |
| 9 | **Names against ids.** `john_pepys_house` is named "Father House", `john_crews_house` "Mr Crews House" — a disjunction between how Pepys referred to people and their most specific historical name. | As drafted. Noted, never ruled on. |

## A2. From the schema work, 7 November 2026

| # | Question | Why it needs you |
|---|---|---|
| 10 | **Principle 4 against the two place-qualified `_unknown_` ids.** `cliff_unknown_deal` (your instruction) and `dutch_ship_unknown` (your review) both depart from `<type>_unknown_<number>`. | Principle 4 and these two ids cannot both be right as written. Either rewrite the principle to allow the qualified form, or renumber the two ids. `validate.py` accepts both and warns on the qualified form so it stays visible. |
| 11 | **Curatorial warnings still sitting in `notes`** — "kept distinct from chequers_inn", "A fourth Chequer, distinct from …". | By your ruling `notes` is yours and gets rewritten freely, so these are exposed to exactly the loss the evidence column was created to repair. If they should be stable they want a home in `evidence` or a column of their own. |
| 12 | **`tavern_unknown_3` has been reused.** The number was the Hague tavern of 17 May, freed when you renamed it `thomas_fuller_lodging`; the 14 June unnamed tavern now holds it. | Keeps the family contiguous and the validator quiet, but a reused number is a trap for anyone citing an id. Say if you would rather have a gap. |

## A3. From the June 1660 draft

| # | Question | Why it needs you |
|---|---|---|
| 13 | **"my Lord's" against "my Lord's lodgings", 11–22 June.** The bare phrase is drafted to `john_crews_house`, the fuller phrase to `sandwich_lodgings`. | That reads two phrasings as two places inside one fortnight. The diary supports it — "the first night of his coming to Whitehall **to lie**" (25 June) and "my Lord's **at Mr. Crew's**" (19 June) — but if they are meant to be one place, 13 and 18 June need re-pointing. **The month's biggest single call.** |
| 14 | **Rochester and Chatham, 8 June.** Drafted in road order — Sittingbourne, Chatham, Rochester, Gravesend — although the entry names Rochester first. | network4 avoided the question by merging them into one node. |
| 15 | **Which Sun, 22 June.** "dined alone at the Sun Tavern", with four Suns in the data. Taken as `sun_tavern_king_street`, nearest where he was. | A guess, and nothing in the entry narrows it. |
| 16 | **Which Leg, 29 June.** "meeting Mr. Townsend in the Palace, he and I … dined at the Leg **there**." | "There" suggests a Leg inside the Palace; drafted as `leg_tavern_king_st`, the adjacent street. |
| 17 | **Which Bell, 23 June.** "to deliver him the horse of Dixwell's that had staid there fourteen days at the Bell." | Taken as `bell_tavern`, on the reading that Mr Holmes was at the Bell. |
| 18 | **The Exchequer is now the King's Head.** 20 June, "at Charing Cross, now the King's Head Tavern", recorded as a `variants` entry on `exchequer_tavern_charing_cross`. | If the reading is wrong, a fifth Charing Cross tavern is missing. network4 drafted it as a separate node. |
| 19 | **Rooms inside a complex.** `shield_gallery_whitehall` is a node; the Nursery of 28 June is folded into `sandwich_lodgings` as a room of that lodging. | Principle 10 (precision inside a complex) argues for a node; the no-cabin rule argues against. The two are drafted inconsistently and should not stay that way. |
| 20 | **Mrs Brown's, 18 June.** "He went to Mrs. Brown's" — my Lord. Pepys is drafted as going too, since they leave for Stepney together. | The entry does not say he went. |

---

# B. Rules in force

Claude applies these without asking. Each was settled by the team; the dated
history is in `DECISIONS.md`.

## B1. Schema and mechanics

| Rule | Detail |
|---|---|
| **Old Style years** | 1 Jan – 24 Mar carries a split year, `1659/60`. From 25 March it is a plain `1660`. Enforced by `validate.py`. |
| **Edge `id`** | **Contiguous**, in row order, from `100001`. Inserting or removing a leg mid-month renumbers everything after it, so an id is good only within the version of the file it was read from. Cite a date and a leg, never an id, where the reference must last. |
| **One file per year** | `network-data/curated/edges_<year>.csv`, by calendar year. January 1659/60 lives in `edges_1660.csv` with the year string intact. |
| **Nodes are cumulative** | One `nodes.csv` for the whole project, never split by year. |
| **Continuity** | Every departure leaves the previous arrival, within a day and across consecutive days. A night away from home is modelled, not assumed. |
| **Days with no movement** | Contribute no edges. |
| **`mode`** | `walk`, `coach`, `boat`, `horse`, `wagon`, `sedan`, `cart`, `ship`. `walk` is the default where the diary names no mode. `boat` covers wherries, barges and schuits. Extend the list deliberately. |
| **`companions`** | `; `-separated; only people who travelled *with* Pepys. Someone met at the destination is not a companion. Standardised names ("Elizabeth Pepys", not "my wife"); role descriptors where no name is known. |
| **Named watermen and coachmen** | Count as companions where Pepys names them. |
| **Unknown places** | `<type>_unknown_<n>`, numbered sequentially per type across the whole project, never restarted per month. Two place-qualified exceptions exist — see A2 #10. |
| **Each unnamed stop is its own node** | Repeated unnamed stops in one area do not share a node. |

## B2. Who owns which column

| Column | Holds | Whose |
|---|---|---|
| `evidence` | The diary passage warranting the identification, quoted, with its date | Claude drafts, GRA verifies |
| `notes` | Locational and curatorial gloss, supporting the coordinate work | **GRA only. Claude does not write here.** |
| `variants` | The diary's other spellings for the same place, `; `-separated | Claude drafts, GRA rules |
| `latitude` / `longitude` | Coordinates | **GRA only. Claude leaves blank, never guesses.** |

A variant that merely restates the node's name is worse than no variant: it
manufactures false collisions in the duplicate check.

## B3. Ships

| | |
|---|---|
| Node for a vessel | `the_` plus the vessel's name — `the_naseby`, `the_london`. The prefix keeps the ship *London* apart from `city_of_london`. |
| `mode` for water travel | Always `boat`. Never the ship's name; there is no `ship` mode in use. |
| When a ship is a location | At embarking and disembarking only. While Pepys is aboard and she sails he changes no node, so no edge arises. |
| Anchorages | Not nodes. Where Pepys disembarks, the node is the ship. |
| Cabins, decks, round-houses | Not nodes. |
| A renamed vessel | One node with a note. The *Naseby* becomes the *Charles* on 23 May 1660; the *Speaker* becomes the *Mary*. |
| 30 March 1660 | Pepys does **not** board the *Naseby*. |

**Fleet movement is deliberately invisible.** Ruled 10 November 2026:
"Continue with the current conventions." The silent days of the voyage — 24–31
March, 26 days of April, 20 days of May, 1–7 June — are correct, not a gap.

## B4. Place identifications

Each holds until superseded by a dated successor.

| Diary phrase | Node | Period |
|---|---|---|
| "home" | `home_axe_yard` | from 1 Jan 1659/60 |
| "my office", "the office" | `office_exchequer` | Jan 1659/60 – |
| "Mrs. Jem", "my Lord's lodgings" | `sandwich_lodgings` | Jan 1659/60 |
| "Mrs. Jem", "Mrs. Ann" | `scott_house` | Feb – 15 Mar 1659/60 |
| "my Lord's lodgings" *in so many words* | `sandwich_lodgings` | from 1 Jan 1659/60 |
| "my Lord's", "my Lord" | `john_crews_house` | 17–21 Mar 1659/60 |
| "my Lord's lodging at the gate" | `sandwich_lodgings` | 22–23 Mar 1659/60 |
| "my Lord's", "my Lord" | `john_crews_house` | 11–22 Jun 1660 *(provisional — A3 #13)* |
| "my Lord's lodging(s)" | `sandwich_lodgings` | from 25 Jun 1660 |
| "my father's" | `john_pepys_house` | from 1 Jan 1659/60 |
| "Mr. Calthrop's", "the Temple" | `lestrange_calthorpe_chamber` | from 2 Jan 1659/60 |
| "Will's" | `wills_alehouse` | from 2 Jan 1659/60 |
| "Catan" | `kate_petit_house` | 13 Jan 1659/60 |
| "the Sun" | `the_sun_tavern` (Chancery Lane) | 20 Jan 1659/60 |
| "the Sun" | `sun_tavern_king_street` | 16 Feb 1659/60 |
| "Mr. Downing's Counsellor", "the Counsellor at the Temple" | `stephens_chamber_temple` | from 1 Feb 1659/60 |
| "Mr. Gunning", "Mr. Gunning's chapel" | `exeter_house_chapel` | from 1 Jan 1659/60 |
| "the park" | `park_unknown_1` | 17 Feb 1659/60 |
| "the Exchange" | `new_exchange` (the Strand) | Feb 1659/60 onward, **but see C2** |

### Places kept deliberately apart

- **Four Chequers**: `chequers_inn` (Charing Cross), `exchequer_tavern_charing_cross`
  (Charing Cross), `chequer_inn_fowlmere`, `chequer_inn_holborn`.
- **Four Suns**: `the_sun_tavern` (Chancery Lane), `sun_tavern_king_street`,
  `sun_tavern_threadneedle_st`, `sun_tavern_fish_street_hill`.
- **Four Swans**: `swan_inn` (New Palace Yard), `swan_tavern_king_st`,
  `the_swan_pub` (Old Fish Street), `swan_tavern_dowgate`.
- **Two Pope's Heads**: `popes_head_tavern_chancery_lane`, `popes_head_alley`.
- **Three Three Tuns**: `three_tuns_tavern` (Guildhall Yard),
  `three_tuns_tavern_charing_cross`, `three_tuns_tavern_cambridge`.
- **Mr Swan's house** is not the Swan tavern.
- **Mr Pierce the purser** is not Mr Pierce the surgeon.
- **`roberts_whitehall`** and **`anthony_robins_whitehall`** are two houses.
- **The Temple is divided finely**: use the precise location where the diary
  gives one, area-level `the_temple` where it does not.

---

# C. Standing instructions

Things to do every time, not one-off rulings.

## C1. Flag for manual dating

- **Combined entries.** Two diary entries cover several days at once: July 1661
  has "8th, 9th, Loth, 11th, 12th, 13th." (six days) and "16th, 17th, 18th,
  19th." (four). Their edges need human dating from a manual read.
- **1–10 October 1668** has no entries in Wheatley. Confirmed a genuine gap in
  the source, not a parsing artefact. There will be no edges.

## C2. Flag for manual check

- **Every "the Exchange" reference.** New or Old, Royal or the Strand arcade —
  each occurrence is checked by hand rather than inferred.
- **Named waypoints on long journeys.** Claude drafts a node where the entry
  names a place passed through on a ride; each wants approval.
- **The renaming of a vessel**, at the date it happens.

## C3. Changes expected later — do not apply early

- **17 July 1660**: Pepys moves from Axe Yard to the Navy Office house in
  Seething Lane. "Home" becomes a new node from that date, and the move itself
  is an edge. *(Bears on A1 #1.)*
- **From July 1660**: "my office" becomes the Navy Office. During Aug–Dec 1660
  "the office" at Whitehall means the Privy Seal Office.
- **September 1666**: the Fire destroys much of the City. Places that move
  afterwards become new nodes.

---

# D. The decision record

Every decision made so far, in the order the chunks were drafted, with the
question as it was put and the ruling as it was given. Decisions already
answered are kept here in full rather than summarised, so this file is the
record and nothing has to be reconstructed from `DECISIONS.md`.

**Legend:** ✅ ruled · ⏳ still open (cross-referenced to section A) ·
↩︎ later superseded.

---

## D1. January 1659/60 — migration

The month was migrated from the workbooks unchanged; `validate.py` then
reported 77 errors. The corrections were applied in the same commit as the
migration, so they are not visible as a git diff. **Spot-checked and confirmed
correct.** After: 77 nodes, 294 edges, 0 errors. Full detail in
`network-data/curated/january-corrections.md`.

| | Decision |
|---|---|
| ✅ | **53 edge endpoints had drifted from the node ids.** `wills_ale_house`→`wills_alehouse` (28 edges), `george_downings_lodging`→`...lodgings` (15), `mr_mossum_church`→`robert_mossum_church` (4), `mother_lams`→`mother_lams_pub` (2), `the_half_moon`→`the_half_moon_alehouse` (2), `william_fuller_lodgings`→`...lodging` (1), `tower_of_menagerie`→`tower_menagerie` (1). Edge endpoints renamed to the canonical node id; **no node ids changed.** These also caused 17 of the 18 continuity breaks. |
| ✅ | **Two nodes were missing entirely.** `the_sun_pub` (The Sun, Chancery Lane; 20 and 23 Jan) and `richard_sherwin_office` (27 Jan) added. |
| ✅ | **One trip was missing, 13 January.** "Thence I went to Mrs. Jem" — `home_axe_yard → sandwich_lodgings`, walk, added. network4 reads the day the same way. |
| ✅ | **One companion casing fixed:** "Clerk of Sandwich troop" → "Clerk of Sandwich Troop". |

### Early rulings arising from January

| | Question | Ruling |
|---|---|---|
| ✅ | `peter_gunning_church` vs `exeter_house_chapel` — one place or two? | **One.** "Call them Exeter House Chapel." `peter_gunning_church` retired; its two 29 January edges repointed. |
| ✅ | `the_new_market` vs `market_unknown_1` — do these overlap? | **No.** |
| ✅ | `city_of_london`'s `name` field held a query, "Referencing the Royal Exchange?" | Resolved; the uncertainty moved out of the name. |
| ✅ | Several nodes share coordinates (`john_pepys_house` and `turner_house` are both Salisbury Court). | **Intended behaviour.** |
| ✅ | Should role descriptors like "Clerk of Sandwich Troop" be kept as companions? | **Yes, keep them.** |
| ⏳ | Names against ids — `john_pepys_house` is named "Father House", `john_crews_house` "Mr Crews House". | A disjunction between how Pepys referred to people and their most specific historical name. Noted, never ruled. *(A1 #9)* |

---

## D2. 1–15 February 1659/60

Drafted by Claude, validated clean. All nine were ruled.

| | Question | Ruling |
|---|---|---|
| ✅ | **1. Is "Mrs. Jem" at `sandwich_lodgings`?** 1 Feb makes them two places; 4 Feb puts Mrs Jem at Scott's. | **`scott_house`.** Eighteen February endpoints moved, covering 1, 3, 6, 7, 8, 9, 13, 14, 15 Feb. The one explicit "my Lord's lodgings" (1 Feb) stays. Extended to Mrs Ann on the strength of 4 and 6 Feb. |
| ✅ | **2. How finely should the Temple be divided?** Four nodes against network4's one. | **Keep them separate.** Use the precise location when given; area-level labels are acceptable when it is not. |
| ✅ | **3. Same for Westminster and Whitehall** — `palace_yard_westminster` is unavoidably vague. | **Correct as drafted.** |
| ✅ | **4. The Chequers** — is "the Exchequer at Charing Cross" the same house as "the Chequers"? | **Two.** `exchequer_tavern_charing_cross` added for 2 Feb. |
| ✅ | **5. Is `downings_counsellor_chamber` the same as `stephens_chamber_temple`?** | **Merge** for these dates into `stephens_chamber_temple`. |
| ✅ | **6. "The Exchange", 11 February** — New or Royal? | **`new_exchange` is correct for February.** Standing instruction: every Exchange reference is flagged for human check. *(now C2)* |
| ✅ | **7. An unnamed drinking stop was inferred** to keep the walk continuous (4 Feb). | **Accept the inference.** |
| ✅ | **8. Out-of-order narration, 13 February** — drafted on the sequence described, not narrated. | **Yes**, that is the general rule. |
| ✅ | **9. Mr Swan's house vs the Swan tavern.** | **Distinct locations.** |
| ✅ | `house_of_commons` was left unused after the review folded its one visit into `westminster_hall`. | **Retire it.** |
| ✅ | Named watermen and coachmen as companions — the principle postdated the February draft. | Earlier months **manually checked**. |

---

## D3. 16–29 February 1659/60 — the Cambridge journey

116 edges, 26 new places. One unbroken walk: London → Foulmere → Cambridge
(three nights at the Falcon) → Saffron Walden and Audley End → Epping → London.

| | Question | Ruling |
|---|---|---|
| ✅ | **1. Which Sun, 16 February?** | **Two Suns.** 16 Feb is the Sun on King Street — `sun_tavern_king_street` — separate from `the_sun_tavern`, Chancery Lane. |
| ✅ | **2. "the park", 17 February** — drafted `st_james_park`. | **`park_unknown_1`.** 3 and 12 Feb keep `st_james_park`. |
| ✅ | **3. Mr Moore's dinner, 19 February.** | **Keep as `john_crews_house`.** |
| ✅ | **4. "my partner", 20 February** — no name given. | **Keep the descriptor** "Pepys's office partner". |
| ✅ | **5. Mr Wotton has no first name.** | **Correct** as drafted. |
| ✅ | **6. Unnamed alehouses — new node or shared?** | **Each occasion gets its own node.** Reused nodes fixed by hand. |
| ✅ | **7. Boat landing, 29 February** — unnamed, drafted `city_of_london`. | **Correct.** |
| ✅ | **8. Named waypoints on the road** — `ware` is a node, network4 omits it. | **Correct.** Standing instruction: flag named waypoints on long journeys for approval. *(now C2)* |
| ✅ | **9. Three Chequers, all distinct?** | **Confirmed separate.** |
| ✅ | **10. The White Hart's master as a companion** (a role descriptor). | **Correct.** |
| ✅ | **11. "the Old Exchange", 28 February** — read as `royal_exchange`. | **Correct.** |
| ✅ | **12. Queens' College is not a node** — an affiliation, not a place visited. | **Correct.** |

Six node ids renamed in the edges during review were synced back to
`nodes.csv`: `wotton_shop`→`william_wotton_shop`,
`mrs_michells_shop`→`anne_michell_shop`, `ware`→`ware_hertfordshire`,
`puckeridge`→`puckeridge_hertfordshire`,
`chequer_inn_foulmere`→`chequer_inn_fowlmere`,
`angier_house_cambridge`→`john_angier_house_cambridge`. One read
`ware_hertforshire`, a missing "d", which had broken 24 February's continuity.

---

## D4. 1–15 March 1659/60

128 edges against network4's 124 over the same fifteen days.

| | Question | Ruling |
|---|---|---|
| ✅ | **1. "my Lord's lodgings" or "my Lord at Mr Crew's"?** 6 March distinguishes them. network4 read it the opposite way; the choice changed six edges in this chunk alone. | **Unqualified "my Lord's lodgings" and "my Lord's" (1, 9, 13, 14, 15 Mar) → `sandwich_lodgings`; the explicit "at Mr. Crew's" (2, 6, 7 Mar) → `john_crews_house`.** Manually checked. |
| ✅ | **2. Mrs Jem in March** — does the February ruling carry? | **Yes. She remains at `scott_house` for 1–15 March.** |
| ✅ | **3. Four Sun taverns now** — each named with its own location. | **Correct**, four houses. |
| ✅ | **4. "the Swan tavern", 2 March** — drafted `swan_inn`, though the party had come from the Leg in King Street. | **A new node:** `swan_tavern_king_st`. Applied 7 Nov 2026; the two 2 March legs repointed, the other 20 `swan_inn` legs untouched. |
| ✅ | **5. Mr Pierce the purser is not Mr Pierce the surgeon.** | **Correct, not the same person.** |
| ✅ | **6. "we three", 4 March** — the third taken to be Jane Birch. | **Correct.** |
| ✅ | **7. Shott's, 8 March** — drafted as `whitehall_palace`. | **Not Whitehall.** A separate node, `shotts_woodmonger_whitehall`. |
| ✅ | **8. 8 March does not say he went home** — a closing leg was added. | **Correct.** |
| ✅ | **9. "the Exchange", 12 March** — read as `new_exchange`. | **Correct.** |
| ✅ | **10. Three more unnamed alehouses** — the series is growing fast. | **Yes, continue.** |
| ⏳ | **11. `lion_tavern` and `cock_tavern` have no location.** | Humans will check by hand. *(A1 #8)* |
| ⏳ | **12. `navy_office` exists; Pepys moves into the adjoining house in July 1660.** | Flagged so the split is deliberate when we reach it. *(A1 #1 — due now)* |

---

## D5. 16–31 March 1659/60

67 edges over 16–23 March; 193 curated edges for the month against network4's
191. **24–31 March carry no edges**: Pepys boards the *Swiftsure* on the 23rd
and changes no node again that month.

| | Item | Outcome |
|---|---|---|
| ✅ | **Five nights at Mrs Crisp's**, 17–21 March, each modelled so the run is continuous. | As drafted. |
| ✅ | **Pepys corrects his own dating, 20–21 March**: "which by a mistake I have put down yesterday". Drafted on the 21st. | As drafted. |
| ✅ | **22 March, the leave-takings.** The first draft compressed them; the cross-check showed network4 modelling four visits this draft lacked. Three had named places. | Day grew 8 → 11 edges. |
| ⏳ | **Kate Sterpin**, 22 March — "took leave of Kate Sterpin" gives no place. | Unmodelled. *(A1 #5)* |
| ✅ | **"Tony Robins's", 19 March** — drafted as the same house as "Roberts at Whitehall". | **A separate house.** `anthony_robins_whitehall` created in review. |
| ✅ | **A fourth Chequer:** `chequer_inn_holborn`. | Accepted. |
| ✅ | **Two Pope's Heads:** `popes_head_tavern_chancery_lane` and `popes_head_alley`. | Accepted. |
| ✅ | **"my Lord" on 22 March** — unqualified, so sent to `sandwich_lodgings`. | Refined in review: 17–21 March → `john_crews_house`; 22–23 March stays `sandwich_lodgings` ("my Lord's lodging **at the gate**"). |
| ✅ | **20 March, the flood.** "boats rowed in King Street and all our yard was drowned"; `westminster_hall` stands in. | As drafted. |
| ✅ | **Named watermen** — "I got Crockford to carry me over it". First clean case. | Companion, mode `boat`. |
| ✅ | **Two more unnamed stops**, each its own node per D3 #6. | As drafted. |

### From the 16–23 March review, 2 November 2026

| | Item | Outcome |
|---|---|---|
| ✅ | **8 March, the Commons lobby leg removed.** "sending a note to my Lord, **he comes out to me**" — Pepys never went in. | A correct catch against the draft. |
| ✅ | **Three node renames completed**, each half-applied in the edges: `crisp_house`→`crisp_house_axe_yard`, `jervas_barber`→`richard_jervas_barber`, `blagrave_house`→`thomas_blagrave_house`. | Synced. |
| ✅ | **One companion spelling normalised:** "Edward Sheply" → "Edward Shipley". | Applied. |
| ⏳ | **Seven companion near-misses** found by the new fuzzy check. | Untouched; canonical spelling is a curatorial call. *(A1 #3)* |
| ⏳ | **Two identifications made for one day only** — "Mr Thomas"/"Thomas Crew", "Mr Woodfine"/"Thomas Woodfine". | Not propagated. *(A1 #4)* |
| ⏳ | **6 March no longer records the visit to Mrs Jem**, which sits against D4 #2. | Flagged, not reverted. *(A1 #2)* |

---

## D6. Ships — settled 28 October and 2 November 2026

Seven questions were asked in October; two October answers were retracted in
favour of README principles 13–14, and the rest confirmed.

| | Question | Ruling |
|---|---|---|
| ✅ | **1. When does `mode` take the value of a ship?** | **Never. `mode` is `boat`** for all water travel. |
| ✅ | **2. Is an anchorage a node?** | **No.** An anchorage is a node only where Pepys disembarks, and there the node is the ship. 23 March reads `tower_of_london → the_swiftsure` with Long Reach in the notes. |
| ✅ | **3. Movement within a ship** — cabins, decks, round-houses. | **One location. No cabin or deck nodes.** |
| ✅ | **4. One node per named vessel.** | **Correct**, each named ship is a node. |
| ✅ | **5. The *Naseby* renamed on 23 May** — one node or two? | **One node with a note**; flag at the renaming. Applied to the *Naseby*→*Charles* and the *Speaker*→*Mary*. |
| ✅ | **6. 30 March — was Pepys aboard the *Naseby*?** | **No.** The day carries no `the_naseby` edge. |
| ✅ | **7. "the Ship tavern", 23 March** is a tavern, not a vessel. | Noted; Pepys did not go in. |
| ✅ ↩︎ | **Ship node naming.** README 14 gave the bare vessel name, which made the *London* collide with `city_of_london`. | **`the_` prefix**, 2 Nov 2026: `the_swiftsure`, `the_naseby`, `the_london`, `the_speaker`, `the_assistance`. 15 edges and 5 crosswalk rows followed. README 14 now reads "e.g. the_naseby". |

Note: the prefix is **not** a reliable marker of a ship — `the_sun_tavern`,
`the_half_moon_alehouse`, `the_swan_pub` and `the_temple` all carry it. A ship
is identified by its node row, not its id.

---

## D7. Applied 28 October 2026

| | Item |
|---|---|
| ✅ | **Edge ids renumbered contiguously**, `100001`–`100722`, no gaps; 263 rows changed id. Supersedes the stable-key rule used to October 2026. The cost is on the record: an id is good only within the version of the file it was read from, and three already-annotated worksheets cite numbers that no longer line up. |
| ✅ | **`house_of_commons` retired** (D2). |
| ✅ | **`shotts_woodmonger_whitehall` created** and the 8 March legs repointed (D4 #7). |
| ✅ | **Eight more half-applied renames synced** to `nodes.csv`: `laxton_apothecary`→`john_layton_apothecary` (also Laxton→Layton), `leg_tavern`→`leg_tavern_king_st`, `pinkney_house`→`george_pinkney_house`, `painted_chamber`→`painted_chamber_westminster`, `rawlinson_house`→`daniel_rawlinson_house`, `blackburne_house`→`robert_blackborne_house` (also Blackburne→Blackborne), `creeds_chamber`→`john_creed_chamber`, `fish_street`→`fish_street_london`. |

---

## D8. April 1660

10 edges over 4 days, 7 new places. **26 of 30 days carry no edges.** network4
read the same month independently and got 9 edges over the same 4 days.

| | Item | Outcome |
|---|---|---|
| ✅ | **1. `london` collides with `city_of_london`.** | Settled by the `the_` prefix (D6). |
| ⏳ | **2. 3 April, an aborted landing** — "we could not stay for fear of not getting into our boat again". | No edge. *(A1 #6)* |
| ✅ | **3. `deal` as a shore node, 30 April** — the one edge by which this draft exceeds network4's. | As drafted. |
| ✅ | **4. "the Captain", 24 April** read as Captain Cuttance, the *Naseby*'s own captain. | As drafted. |
| ✅ | **5. The *Naseby* renaming** flagged forward to May. | Handled per D6 #5. |
| ⏳ | **6. Everyone else moves and Pepys does not** — Shipley to Sheppy, Stayner to Dover, Burr ashore, none an edge. | Correct, since the network records Pepys. Worth confirming for the voyage. *(A1 #7)* |
| ✅ | **7. Within-ship places named and not modelled** — the Round-house, the coach, the great cabin, the half-deck table. | Per D6 #3. |

---

## D9. May 1660

67 edges over 11 days, 33 new nodes, against network4's 63 over the same days.

| | Item | Ruling |
|---|---|---|
| ✅ | **1. Three ships the diary will not name.** Stayner's (3 May) and the Rear-Admiral's (22 May) drafted as one `ship_unknown_1`, choosing identity over caution. | **Split in review:** `dutch_ship_unknown` created for 22 May. |
| ✅ | **2. Five nights ashore in Holland**, 14–19 May, folded into one `lodging_unknown_1` on the strength of "**our** lodging". | Manually checked. |
| ✅ | **3. Ten unnamed places of new types** — May needed more `_unknown_` nodes than every previous month together. | Accepted. |
| ✅ | **4. "the Dr.'s", 17 May** — the tavern he had sent Dr Fuller to, or Dr Fuller's own lodging? | **Dr Fuller's lodging:** `thomas_fuller_lodging`. Manually checked. |
| ✅ | **5. The cliff of 29 May is not Dover** — the barge lay at Deal, the fleet was visible from the top, and it measured "not above thirty-five yards". network4 called it `dover_cliff`. | **Rename to `cliff_unknown_deal`.** |
| ✅ | **6. The 22 May Rear-Admiral's ship** — network4 identified it as the Speaker; 25 April shows both admirals merely dining aboard Captain Clerke's Speaker. | network4 not followed. |
| ✅ | **7. The boat that never landed, 22 May.** | No edge; noted on the surrounding leg. Manually checked. |
| ✅ | **8. Two ships renamed on 23 May** — the *Nazeby* into **Charles** (not *Royal Charles*), the *Speaker* into *Mary*. | One node each with a note, per D6 #5. |
| ✅ | **9. Twenty days with no movement at all** — the third chunk running to raise whether the rules should let fleet movement be recorded. | **"This is correct. Continue with the current conventions."** The question is shut. |

---

## D10. June 1660

197 edges over 23 days, 42 new nodes, against network4's 190. The voyage ends
on the 8th. **All ten flags are awaiting review — see section A3.**

| | Item | Where it stands |
|---|---|---|
| ⏳ | **Where my Lord lodged**, 11–22 June — the bare "my Lord's" to Mr Crew's, the fuller "my Lord's lodgings" to Whitehall. | *(A3 #13)* |
| ✅ | **Pepys changes lodging twice**: his father's 9–21 June, Axe Yard from the 22nd — "To bed, the first time since my coming from sea, in my own house". | As drafted. |
| ✅ | **Four nights closed by inference** (9, 10, 11, 15 June), each noted on the edge. | As drafted. |
| ⏳ | **Rochester and Chatham, 8 June**, drafted in road order against the order narrated. | *(A3 #14)* |
| ⏳ | **Which Sun, which Leg, which Bell** — three unqualified house names. | *(A3 #15–17)* |
| ⏳ | **The Exchequer at Charing Cross is the King's Head** — recorded as a variant, not a new house. | *(A3 #18)* |
| ⏳ | **`tavern_unknown_3` reused** after the Hague tavern was renamed. | *(A2 #12)* |
| ⏳ | **Rooms inside a complex** — `shield_gallery_whitehall` is a node, the Nursery is not. | *(A3 #19)* |
| ⏳ | **Mrs Brown's, 18 June** — the entry says my Lord went, not Pepys. | *(A3 #20)* |
| ✅ | **The Banqueting House, 23 June** — whether Pepys followed the King is not stated. | No edge. |

---

## D11. Schema and tooling

| | Decision | Date |
|---|---|---|
| ✅ | **Edge ids are contiguous**, superseding stable surrogate keys. | 28 Oct 2026 |
| ✅ | **Ship nodes take a `the_` prefix.** | 2 Nov 2026 |
| ✅ | **`nodes.csv` splits into `notes`, `evidence` and `variants`.** Prompted by a coordinate pass overwriting the diary passages on eight nodes. `notes` becomes locational gloss the GRA owns and rewrites freely; `evidence` holds the warrant, quoted with its date; `variants` holds the diary's other spellings. All 106 quotations preserved, the eight overwritten ones recovered. | 7 Nov 2026 |
| ✅ | **Claude does not write in the `notes` column.** | 10 Nov 2026 |
| ⏳ | **`<type>_unknown_<place>` beside `<type>_unknown_<n>`.** Accepted by the validator, warned on, because principle 4 still asks for a number. | *(A2 #10)* |
| ✅ | **The README principles are complete.** Reports that principles 6, 12 and 15 were missing were Claude's error — Markdown renumbers ordered lists on render, so a source reading `1 2 3 4 5 7 8 9 10 11 13 14 16` displays as a consecutive 1–13. Withdrawn 11 Nov 2026. Source and rendered numbering diverge from the sixth principle on; this project cites source numbers. | 11 Nov 2026 |

---

## D12. Standing items with no date

| | Item |
|---|---|
| ✅ | **Combined diary entries.** July 1661 has "8th, 9th, Loth, 11th, 12th, 13th." (six days) and "16th, 17th, 18th, 19th." (four). Their edges are flagged for human dating from a manual read. |
| ✅ | **1–10 October 1668 has no entries** in Wheatley. Confirmed a genuine gap in the source, not a parsing artefact; there will be no edges. |
