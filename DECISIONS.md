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
| **Edge `id`** | **Contiguous**, in row order, from `100001`. Row order carries chronology, and the id follows it, so the sequence is meaningful rather than arbitrary. The cost is that inserting or removing a leg mid-month renumbers everything after it: an id is therefore only good within the version of the file it was read from, and a worksheet or comment citing one goes stale. Cite a date and a leg rather than an id where it needs to last. Settled by the team, superseding the stable-key rule used up to October 2026. |
| **One file per year** | `network-data/curated/edges_<year>.csv`, filed by calendar year. January 1659/60 lives in `edges_1660.csv` with the year string intact. |
| **Nodes are cumulative** | One `nodes.csv` for the whole project. A new month appends to it; it is never split by year. |
| **Continuity** | Travel is unbroken. Every departure leaves the node of the previous arrival, within a day *and* across consecutive diary days. A night spent away from home is modelled explicitly rather than assumed. |
| **Days with no movement** | Contribute no edges. The continuity check skips them (15 January 1659/60 is the first such day). |
| **`mode`** | Controlled vocabulary: `walk`, `coach`, `boat`, `horse`, `wagon`, `sedan`, `cart`, `ship`. `walk` is the default where the diary names no mode. `boat` covers wherries, barges and schuits. Extend the list in `scripts/pepys.py` deliberately, not ad hoc. |
| **`companions`** | `; `-separated. Only people who travelled *with* Pepys on that leg -- someone merely met at the destination is not a companion. Standardised names ("Elizabeth Pepys", not "my wife"). Role descriptors are acceptable where no name is known ("Quartermaster of Sandwich Troop", "unknown man"). |
| **`latitude` / `longitude`** | Human-filled only. Claude leaves them blank rather than guessing. |
| **`notes`** | Claude drafts these from the text (who lived there, how the place was identified, the entry that first mentions it). Factual and checkable; no speculation presented as fact. A genuine uncertainty is written with a question mark. |
| **Unknown places** | `<type>_unknown_<n>` per README principle 4, numbered sequentially per type across the whole project (not restarted each month). |
| **Ships** | A named ship is one location however far she sails, and the node is the vessel's name (`naseby`), with no suffix. Water travel always takes `mode` = `boat` -- never the ship's name, and there is no `ship` mode. A ship is a location when Pepys embarks or disembarks; while he is aboard and she sails he changes no node, so no edge arises. No cabin or deck nodes. README principles 13-14, which supersede the retracted rulings in section 7. |

## 2. Place identifications

Ambiguous place-words change meaning through the diary. Each ruling holds until
superseded by a dated successor.

| Diary phrase | Node | Period | Basis |
|---|---|---|---|
| "home" | `home_axe_yard` | from 1 Jan 1659/60 | Axe Yard, Westminster |
| "my office", "the office" | `office_exchequer` | Jan 1659/60 - | Mr Downing's Exchequer office, Westminster Palace |
| "Mrs. Jem", "my Lord's lodgings" | `sandwich_lodgings` | Jan 1659/60 | Jemima Montagu lodged at the Earl of Sandwich's Whitehall lodgings |
| "Mrs. Jem", "Mrs. Ann" | `scott_house` | Feb 1659/60 | Mrs Jem lodges at the Scotts' through February (section 4 ruling 1). Mrs Ann lodges with her: 4 Feb puts both at Scott's, and 6 Feb has them in the same chamber |
| "my Lord's lodgings" *in so many words* | `sandwich_lodgings` | from 1 Jan 1659/60 | Only where the diary names my Lord's lodgings, not where it names Mrs Jem -- 1 Feb does both, and they are two places |
| "my father's" | `john_pepys_house` | from 1 Jan 1659/60 | John Pepys Sr., tailor, Salisbury Court |
| "Mr. Calthrop's", "the Temple" | `lestrange_calthorpe_chamber` | from 2 Jan 1659/60 | Chancery Lane, Temple district |
| "Will's" | `wills_alehouse` | from 2 Jan 1659/60 | Old Palace Yard |
| "Catan" | `kate_petit_house` | 13 Jan 1659/60 | as read by the project team |
| "the Sun" | `the_sun_tavern` | 20 Jan 1659/60 | "the Sun in Chancery Lane" |
| "Mr. Downing's Counsellor", "the Counsellor at the Temple" | `stephens_chamber_temple` | from 1 Feb 1659/60 | One person acting in the Downing/Squib case (section 4 ruling 5) |
| "Mr. Gunning", "Mr. Gunning's chapel" | `exeter_house_chapel` | from 1 Jan 1659/60 | Gunning preached at Exeter House Chapel (section 3 ruling 1) |
| "the Exchequer at Charing Cross" | `exchequer_tavern_charing_cross` | 2 Feb 1659/60 | Distinct from `chequers_inn`, "the Chequers" (section 4 ruling 4) |

### Changes expected later (do not apply early)

- **17 July 1660**: Pepys moves from Axe Yard to the Navy Office house in
  Seething Lane. "Home" becomes a new node from that date; the move itself is
  an edge.
- **From July 1660**: "my office" becomes the Navy Office, Seething Lane, kept
  as a node separate from the adjoining house. During Aug-Dec 1660 "the office"
  at Whitehall means the Privy Seal Office.
- **23 March - 8 June 1660**: the voyage. Ships are nodes and Pepys lives
  aboard; per README principles 13-14 a ship is one location even while moving,
  and water travel is always `boat`. The
  *Naseby* is renamed *Royal Charles* on 23 May -- same node or two is an open
  question.
- **September 1666**: the Fire destroys much of the City. Places that move
  afterwards become new nodes, per the network-three prompt.

## 3. Open questions

Rulings needed from the project team. Claude should not decide these alone.

1. **`peter_gunning_church` vs `exeter_house_chapel`** -- both exist in
   `nodes.csv`. Gunning preached at Exeter House Chapel, and network4 reads
   29 January as a visit to Exeter House Chapel where the curated data has
   `peter_gunning_church`. Are these one place? yes, call them Exeter House Chapel
   -- **applied**: `peter_gunning_church` retired, its two 29 January edges now
   point at `exeter_house_chapel`.
2. **`the_new_market` vs `market_unknown_1`** -- do these overlap? no.
3. **`city_of_london`** -- the `name` field currently holds a query
   ("Referencing the Royal Exchange?") rather than a name. Resolve, and move
   the uncertainty into `notes`. yes. -- **applied** during the February review.
4. **Names vs ids** -- `john_pepys_house` is named "Father House" and
   `john_crews_house` "Mr Crews House". This reflects a disjunction between how
   Pepys referred to these people and these people's most specific name as historians understand them.
6. **Coordinate granularity** -- several nodes share coordinates (e.g.
   `john_pepys_house` and `turner_house` are both Salisbury Court). This is intended behavior.
7. **Companion roles** -- keep descriptors like "Clerk of Sandwich Troop" as
   companions
8. **Combined entries.** Two entries in the diary cover several days at once:
   July 1661 has "8th, 9th, Loth, 11th, 12th, 13th." (six days) and
   "16th, 17th, 18th, 19th." (four). The edges for these dates should be
   flagged for human dating based on a manual read of the diary.
9. **October 1668.** Wheatley's text has no entries for 1-10 October 1668; it
   resumes on the 11th. This is confirmed as a genuine gap in the source, not a parsing
   artefact -- there will be no edges for those days.

---

## 4. Flagged in the 1-15 February 1659/60 draft

Drafted by Claude, validated clean, awaiting your review. Each of these is a
judgement call, not a mechanical question -- please rule, and the ruling moves
up into section 2 or 3.

1. **"Mrs. Jem" may not be at `sandwich_lodgings` in February.** Section 2
   equates them, but 1 February reads "from thence to Mrs. Jem ... Thence home
   and took Gammer East, and James the porter ... to my Lord's lodgings",
   which makes them two places; and 4 February has "to Scott's, where Mrs. Ann
   was in a heat ... but told Mrs. Jem what I had done", which puts Mrs Jem at
   Scott's. Drafted per the existing ruling, which produces a
   home -> lodgings -> home -> lodgings shuttle on 1 February. **Does Mrs Jem
   need her own node?** Yes, Mrs Jem is staying at the Scott house in February.
2. **How finely should the Temple be divided?** The draft has four nodes in the
   Temple district -- `lestrange_calthorpe_chamber` (from January), `the_temple`
   (area level, where no chamber is named), `stephens_chamber_temple` and
   `temple_gardens`. Network4 collapses all of them into one. README principle
   10 favours precision, principle 11 allows area-level labels; this is the
   boundary between them. Yes keep them separate, use precise location in the Temple when given, area-level labels are acceptable when specific location is not provided.
3. **Same question for Westminster and Whitehall.** The draft adds
   `guard_chamber_whitehall`, `palace_yard_westminster`, `house_of_commons`,
   `commons_lobby` and `upper_bench_court`. `palace_yard_westminster` is
   unavoidably vague -- the 3 and 6 February entries say only "the Palace
   Yard", not which one. This is correct. 
4. **The Chequers.** The draft treats "the Exchequer at Charing Cross" (2 Feb)
   and "the Chequers" (5 and 11 Feb) as one house, `chequers_inn`. Network4
   keeps them apart as two taverns. One node or two? Two.
5. **`downings_counsellor_chamber` may be `stephens_chamber_temple`.** On
   1 February Pepys goes to "Mr. Downing's Counsellor"; on 4 February to "the
   Counsellor at the Temple, Mr. Stephens", and on 10 February "Mr. Stevens our
   lawyer" acts in the same Downing/Squib case. Drafted as two nodes to avoid
   asserting the identification. **Merge?** Yes merge for these dates to stephens_chamber_temple.
6. **"The Exchange", 11 February** -- drafted as `new_exchange` (the Strand)
   rather than `royal_exchange` (the City), because the walk starts from Axe
   Yard after ten at night; network4 reads it the same way. January's data uses
   `royal_exchange` for its Exchange references, so this may want revisiting
   there too -- and it bears on open question 3, the `city_of_london` node whose
   name still reads "Referencing the Royal Exchange?". new_exchange is correct for February, references to the exchange should be flagged for human check based on a manual read of the diary.
7. **Inferred a place that is not named.** On 4 February, "we met with an
   acquaintance of his in the walks, and went and drank" became
   `alehouse_unknown_4` near Gray's Inn, to keep the walk continuous. Accept
   the inference, or should an unnamed drinking stop be folded into the
   preceding node? Yes accept the inference.
8. **Out-of-order narration, 13 February.** "I went to Mr. Fage from my
   father's" appears at the very end of the entry, after Pepys has already gone
   home. Drafted on the sequence the sentence describes (father's -> Fage's ->
   father's -> home) rather than the order the text presents it in. Is that the
   right general rule for retrospective sentences? Yes.
9. **Mr Swan's house vs the Swan tavern.** The draft reads "to Mr. Swan's"
   (4 Feb) and "I went to Mr. Swan" (10 Feb) as his house, `swan_house`,
   separate from `swan_inn`, the tavern in New Palace Yard. Network4 reads at
   least one of these as the tavern. These are distinct locations.

### Applied

Rulings 1-9 above are settled. The four that needed data changes have been made:

- **Ruling 1** -- eighteen February endpoints moved from `sandwich_lodgings` to
  `scott_house`, covering every "Mrs. Jem" and "Mrs. Ann" visit on 1, 3, 6, 7,
  8, 9, 13, 14 and 15 February. The single February reference to "my Lord's
  lodgings" in so many words (1 Feb, edges 100303-100304) stays at
  `sandwich_lodgings`. This resolves the shuttle the flag described: 1 February
  now reads Wright's -> Scott's -> home -> my Lord's lodgings, and the entry
  names Madam Scott and her husband at the Mrs Jem visit, which corroborates it.
  **Note for the team:** the ruling named Mrs Jem; extending it to Mrs Ann is an
  inference from 4 February ("to Scott's, where Mrs. Ann was in a heat ... but
  told Mrs. Jem what I had done") and 6 February, which put them in one chamber.
  Say if Mrs Ann should be treated separately.
- **Ruling 4** -- `exchequer_tavern_charing_cross` added for 2 February;
  `chequers_inn` keeps 5 and 11 February.
- **Ruling 5** -- `downings_counsellor_chamber` retired into
  `stephens_chamber_temple`.
- **Rulings 2, 3, 6, 7, 8, 9** needed no change; the draft already matched.

### Still to settle

- **`house_of_commons` is now unused.** The review folded the 3 February
  "Houses sitting" visit into `westminster_hall`, which leaves the node with no
  edges, sitting awkwardly against ruling 3's endorsement of the Westminster
  subdivision. Keep it for later months, or retire it? retire it.
- **Principle 13** (named watermen and coachmen count as companions) was added
  to `README.md` after the February draft was written. February applies it where
  the review added names; earlier months have not been swept for it. Manually checked earlier months.

---

## 5. Flagged in the 16-29 February 1659/60 draft

The Cambridge journey. 116 edges, 26 new places, validated clean, and the whole
fortnight forms one unbroken walk: London -> Foulmere (night of 24th) ->
Cambridge, three nights at the Falcon, -> Saffron Walden and Audley End ->
Epping (night of 27th) -> London.

1. **Which Sun Tavern, 16 February?** Drafted as `the_sun_tavern`, Chancery
   Lane, the only Sun in the node list -- but the company is Exchequer
   colleagues setting out from Will's in Westminster, and network4 keeps a
   separate Sun in Westminster. One house or two? Two, the sun tavern 16 February refers to the sun tavern on King St. This is separate from 'the_sun_tavern' Chancery Lane.
2. **"the park", 17 February** -- drafted as `st_james_park`, consistent with
   3 and 12 February, though this walk starts from Exeter House in the Strand
   rather than from Axe Yard. park_unknown_1 for 17 February.
3. **Mr Moore's dinner, 19 February** -- "went home with him to dinner" drafted
   as `john_crews_house`, on the strength of the secluded members coming in "to
   Mr. Crew" after that dinner. If Moore had lodgings of his own, this is wrong.
4. **"my partner", 20 February** -- recorded as the descriptor "Pepys's office
   partner" for want of a name. Possibly Mr Hawly. A name would be better.
5. **Mr Wotton has no first name** (`wotton_shop`, 18 February). The diary gives
   only "Mr. Wotton's", the shoemaker. This is correct.
6. **Unnamed alehouses: new node or shared?** This chunk adds
   `alehouse_unknown_6` (Fleet Street, 18 Feb) and `alehouse_unknown_7`
   (Westminster, 23 Feb). network4 instead reuses an existing alehouse for
   18 February. Should repeated unnamed stops in one area share a node, or does
   each occasion get its own? Each occasion gets its own. Reused nodes have been fixed by human.
7. **Boat landing, 29 February** -- "my wife and I by water to London, and
   thence to Herring's" drafted as home -> `city_of_london` (boat) ->
   `michael_hering_house` (walk). The landing place is not named, so
   `city_of_london` stands in for it under README principle 11. Correct.
8. **Waypoints on the road** -- `ware` is a node because the entry names it
   ("About Ware we overtook Mr. Blayton"); network4 omits it. Confirm that named
   waypoints on a long ride count, as they do in town. Correct, flag nodes for named waypoints on long journeys for human approval.
9. **Three Chequers, all distinct.** `chequers_inn` (the Chequers, Charing
   Cross), `exchequer_tavern_charing_cross` (the Exchequer, Charing Cross) and
   now `chequer_inn_foulmere` (the Chequer, Foulmere, Cambridgeshire). Please
   confirm the third is genuinely separate and not a spelling of one of the others. Confirm, they are separate.
10. **The White Hart's master as a companion.** He walks Pepys and Mr Blayton to
    Audley End and through the almshouse, so he is recorded as "master of the
    White Hart" -- a role descriptor, which section 3 ruling 7 permits. Correct.
11. **"the Old Exchange", 28 February** -- read as `royal_exchange`, the Royal
    Exchange in the City, against the New Exchange in the Strand. Flagged
    because section 4 ruling 6 asks for Exchange references to be checked by
    hand. Correct.
12. **Queens' College is not a node.** network4 creates one for 26 February;
    this draft reads "Mr. Nicholas, of Queen's College" as the preacher's
    affiliation, not a place Pepys went. He heard him at St Botolph's. Correct.

### Applied (section 5)

- **Ruling 1** -- `sun_tavern_king_street` added for 16 February; the Chancery
  Lane `the_sun_tavern` keeps 20 and 23 January.
- **Ruling 2** -- the 17 February park is `park_unknown_1`. 3 and 12 February
  keep `st_james_park`, which the ruling did not disturb.
- **Rulings 5, 7, 8, 9, 10, 11, 12** confirmed the draft as it stood. Ruling 6
  (each unnamed stop gets its own node) matched the draft too.
- `nodes.csv` was brought into line with the six node ids renamed in
  `edges_1660.csv` during review: `wotton_shop` -> `william_wotton_shop`,
  `mrs_michells_shop` -> `anne_michell_shop`, `ware` -> `ware_hertfordshire`,
  `puckeridge` -> `puckeridge_hertfordshire`, `chequer_inn_foulmere` ->
  `chequer_inn_fowlmere`, `angier_house_cambridge` ->
  `john_angier_house_cambridge`. One reference read `ware_hertforshire`, a
  missing "d", which had broken 24 February's continuity.

### Still open from section 5

- **Ruling 3, Mr Moore's dinner on 19 February** was not answered. It stands as
  `john_crews_house`. Keep as john_crews_house.
- **Ruling 4, "my partner" on 20 February** was not answered. It stands as the
  descriptor "Pepys's office partner". Keep "Pepys's office partner".

### Settled: edge ids are contiguous

Section 1 used to call an edge id a stable surrogate key, never renumbered. The
team has ruled for contiguous ids instead, and the 1660 edges have been
renumbered in row order: `100001`-`100722`, no gaps, 263 rows changed id.

What that costs, so it is on the record: an id identifies a row only within the
version of the file it was read from. Inserting or removing a leg mid-month
shifts every id after it. The three review worksheets already annotated
(`1660-02-a`, `1660-02-b`, `1660-03-a`) cite the old numbers and no longer line
up. Cite a date and a leg, not an id, wherever a reference needs to outlive the
next edit.

---

## 6. Flagged in the 1-15 March 1659/60 draft

128 edges, 33 new places, validated clean. The night of 12 March at Mr Bowyer's
in Huntsmore is modelled explicitly, so the fortnight is one unbroken walk.

Cross-checked against network4: 128 edges against their 124 over the same
fifteen days. Nearly every disagreement falls on the first two items below,
which is why they lead.

1. **"my Lord's lodgings" or "my Lord at Mr Crew's"? -- the one that matters
   most.** 6 March distinguishes them: "we both went up to my Lord's lodgings
   at Mr. Crew's, where he bade us to go home again, and get a fire against an
   hour after. **Which we did at White Hall**, whither he came." So my Lord was
   *staying* at Mr Crew's while his own quarters stood at Whitehall. On that
   reading the draft sends unqualified "my Lord's lodgings" and "my Lord's"
   (1, 9, 13, 14, 15 March) to `sandwich_lodgings`, and only the explicit "at
   Mr. Crew's" (2, 6, 7 March) to `john_crews_house`. 
   **network4 reads it the opposite way**, mapping every early-March visit to
   Mr Crew's. Its own notes say so. Both are defensible and the choice changes
   six edges in this chunk alone, more in the rest of March. Please rule. Unqualified "my Lord's lodgings" and "my Lord's"
   (1, 9, 13, 14, 15 March) to `sandwich_lodgings`, and only the explicit "at
   Mr. Crew's" (2, 6, 7 March) to `john_crews_house`. This has been manually checked by humans.
2. **Mrs Jem in March.** Section 4 ruling 1 placed her at `scott_house` "in
   February". The draft carries that into March (2, 6, 10, 14, 15 March), since
   nothing says she moved, but the ruling did not cover it. network4 keeps her
   at `sandwich_lodgings` throughout. Mrs Jem remains at 'scott_house' for 1-15 March.
3. **Four Sun taverns now.** `the_sun_tavern` (Chancery Lane),
   `sun_tavern_king_street`, and this chunk adds `sun_tavern_behind_exchange`
   ("the Sun behind the Exchange", 7 March) and
   `sun_tavern_fish_street_hill` ("the Sun tavern on Fish Street Hill",
   10 and 15 March). Each is named with its own location in the text, so they
   are drafted as four houses. Correct.
4. **"the Swan tavern", 2 March** -- drafted as `swan_inn`, New Palace Yard,
   though the party had just come from the Leg in King Street. 
5. **Mr Pierce the purser is not Mr Pierce the surgeon.** 3 March names the
   purser; `james_pearse_house` is the surgeon's. Recorded as the companion
   "Mr Pierce the purser"; he will need his own node and a first name when
   Pepys visits him. Correct they are not the same person.
6. **"we three", 4 March** -- Pepys, his wife, and the third taken to be the
   maid, Jane Birch, who is named as a companion in January. Correct.
7. **Shott's, 8 March** -- "To Whitehall to bespeak some firing for my father
   at Shott's" is drafted as `whitehall_palace` only. If Shott's is a separate
   shop it needs a node. It is not 'whitehall_palace', manually renamed 'shotts_woodmonger_whitehall' in edges, create new node.
8. **8 March does not say he went home.** The last stated movement is Harper's,
   so a closing leg to Axe Yard was added to keep the day continuous; 9 March
   starts from home. Correct.
9. **"the Exchange", 12 March** -- read as `new_exchange`, the Strand arcade,
   because he is shopping with his wife from Axe Yard. Flagged because section 4
   ruling 6 asks for Exchange references to be checked by hand. Correct.
10. **Three more unnamed alehouses** -- `alehouse_unknown_8` (City, 3 March),
    `alehouse_unknown_9` (Drury Lane, 3 March), `alehouse_unknown_10` (City,
    7 March), each its own node per section 5 ruling 6. The series is growing
    quickly; worth a glance at whether that is wanted at this rate. Yes continue. 
11. **`lion_tavern` and `cock_tavern` have no location.** The entries name
    neither street. Humans will manually check.
12. **`navy_office` now exists**, Seething Lane. Pepys moves into the adjoining
    house in July 1660, and earlier network notes keep house and office as two
    nodes. Flagging now so that split is deliberate when we reach it.

## 7. Ships (superseded by README principles 13-14)

**These questions are answered.** README principles 13 and 14 now carry the
rules, and the two answers written here in October were retracted by the team in
favour of them. The settled version lives in section 1; the questions are kept
below only for the record of what was asked.

The short of it: water travel is always `mode` = `boat`, the node is the
vessel's name with no suffix, and a ship is a location at embarking and
disembarking only. Nothing after 22 March is drafted yet.

1. **When does `mode` take the value of a ship?** While Pepys is aboard and the
   vessel sails, he does not change node, so no edge is created and there is
   nothing to carry the mode. Is `ship` meant for the legs where a named vessel
   carries him between two places he is recorded at ashore, with the small-boat
   trips out to a ship and between ships staying `boat`? Or should the mode name
   the vessel itself (`naseby`) rather than the generic `ship`? 'mode' is 'boat'.
2. **Is an anchorage a node?** 23 March: the barges go "to the Long Reach, where
   the Swiftsure lay at anchor". Principle 12 implies Long Reach is where the
   ship happened to be, not a place visited, so the draft would read
   `tower_of_london -> swiftsure` by boat with Long Reach in the notes. Anchorage is a node only when Pepys disembarks the ship, in which case the node is the name of the ship (e.g. Nazeby). 
3. **Movement within a ship.** "I to the cabin allotted for me", "I supped at
   the deck table". Principle 10 favours precision inside a sprawling complex,
   but principle 12 makes a ship one location. Reading 12 as overriding, so no
   cabin or deck nodes. Confirm. Correct, a ship is one location.
4. **One node per named vessel** -- *Swiftsure*, *Naseby*, and later the
   *London*, *Speaker*, *Plymouth*, *Essex*, *Assistance*, which Pepys visits
   by boat. Confirm. Correct, each named ship is a node.
5. **The *Naseby* is renamed *Royal Charles* on 23 May.** One node with a note,
   or two nodes with an edge-less change of name? The same question will arise
   for Pepys's own moves ashore. One node with a note, flag for manual check.
6. **30 March: was Pepys aboard?** "my Lord and many others went on board her
   [the *Nazeby*]" -- the entry describes her new chimney in detail but does not
   place Pepys among the party. Include the visit or not? No Pepys does not board the Nazeby.
7. **"the Ship tavern", 23 March** is a tavern in London, not a vessel. Noting
   it so the name does not get read as one; Pepys did not go in.

---

## 8. Applied 28 October 2026, and what is still open

### Applied

- **Edge ids renumbered contiguously**, `100001`-`100722`, no gaps; 263 rows
  changed id. Section 1 and `CLAUDE.md` rewritten to match, and the cost is
  recorded there.
- **`house_of_commons` retired.** It had no edges after the February review
  folded the "Houses sitting" visit into `westminster_hall`. network4's
  Parliament House now maps to nothing in the crosswalk.
- **`shotts_woodmonger_whitehall` created** and the 8 March legs point at it,
  per section 6 ruling 7. The review had renamed it in `edges_1660.csv`; the
  node row was missing.
- **`nodes.csv` brought into line with eight more ids renamed in the edges**:
  `laxton_apothecary` -> `john_layton_apothecary` (also Laxton -> Layton),
  `leg_tavern` -> `leg_tavern_king_st`, `pinkney_house` ->
  `george_pinkney_house`, `painted_chamber` -> `painted_chamber_westminster`,
  `rawlinson_house` -> `daniel_rawlinson_house`, `blackburne_house` ->
  `robert_blackborne_house` (also Blackburne -> Blackborne), `creeds_chamber`
  -> `john_creed_chamber`, `fish_street` -> `fish_street_london`.
- **Ship rules folded into section 1** from README principles 13-14, so drafting
  applies them without re-reading section 7.

### Noticed while reviewing

- **README's principle numbering is broken.** Principle 12 was deleted and the
  list now runs 1-11, 13, 14, 16 -- there is no 15, and nothing is numbered 12.
  Worth renumbering, because this file and `CLAUDE.md` cite principles by
  number; the references to "principle 12" have been repointed to 13-14, but
  any new citation will be guessing.
- **6 March no longer records the visit to Mrs Jem.** The review retargeted that
  leg to `sandwich_lodgings` and dropped the following one, so the day reads
  home -> my Lord's lodgings -> the Red Lion -> home. That is a defensible
  reading of an entry whose "dining-room ... full of tag, rag, and bobtail,
  dancing" sounds like my Lord's household rather than the Scotts'. It does sit
  against section 6 ruling 2, which put Mrs Jem at `scott_house` for all of
  1-15 March. Flagging the inconsistency, not reverting it.
- **8 March: the Commons lobby leg was rightly removed.** "sending a note to my
  Lord, he comes out to me" -- Pepys never went in. A good catch against the
  draft.

### Still open

- **Section 6 ruling 4** -- "the Swan tavern", 2 March. The line was edited but
  no ruling written; it stands as `swan_inn`.
- **Section 6 ruling 12** -- whether `navy_office` and the house Pepys moves
  into in July 1660 stay two nodes.
- **Section 7 question 6** -- whether Pepys was aboard the *Naseby* on 30 March.
- **Is a named anchorage a node?** The October answer (yes, if named) was
  retracted along with the rest of section 7, and README 13-14 do not mention
  anchorages. Taking the principles at face value, a ship is the location
  wherever she lies, so 23 March reads `tower_of_london -> swiftsure` by boat
  with Long Reach in the notes, and no `long_reach` node. That is the reading
  the voyage will be drafted on unless the team says otherwise.

