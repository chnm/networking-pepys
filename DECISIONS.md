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
| **Ships** | A named ship is one location however far she sails, and the node is `the_` plus the vessel's name: `the_swiftsure`, `the_naseby`, `the_london`, `the_speaker`, `the_assistance`. The prefix is what keeps the ship *London* apart from `city_of_london`. Water travel always takes `mode` = `boat` -- never the ship's name, and there is no `ship` mode. A ship is a location when Pepys embarks or disembarks; while he is aboard and she sails he changes no node, so no edge arises. No cabin or deck nodes. README principles 13-14, with the prefix settled 2 November 2026. |
| **Anchorages** | Not nodes. An anchorage matters only where Pepys disembarks, and there the node is the ship, not the water she lies in. So 23 March reads `tower_of_london -> the_swiftsure` by boat, with Long Reach recorded in the notes and no `long_reach` node. Section 7 ruling 2. |

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
| "my Lord's", "my Lord" | `john_crews_house` | 17-21 Mar 1659/60 | My Lord was staying at Mr Crew's over those days (section 10) |
| "my Lord's lodging at the gate" | `sandwich_lodgings` | 22-23 Mar 1659/60 | Back in his own Whitehall lodgings for the departure |
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
- **30 March 1660**: Pepys does **not** board the *Naseby*. "my Lord and many
  others went on board her" does not include him, so the day carries no
  `the_naseby` edge even though the entry describes her new chimney. Section 7
  ruling 6.
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
   though the party had just come from the Leg in King Street. New node
   different from swan_inn, name new node swan_tavern_king_st.
   **Applied 7 November 2026**: `swan_tavern_king_st` created at King Street,
   Westminster, and the two 2 March legs re-pointed to it. The other 20
   `swan_inn` legs are untouched, so New Palace Yard keeps every other
   visit. If any of those is also meant to be the King Street house, say
   which dates.
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

### Settled 28 October 2026 (section 7)

All seven ship questions are now answered, so the voyage can be drafted:

| | |
|---|---|
| `mode` for water travel | always `boat` (ruling 1, README 13-14) |
| Node for a vessel | `the_` plus the vessel's name, e.g. `the_swiftsure` (settled 2 Nov 2026) |
| Anchorages | not nodes; the ship is the node where Pepys disembarks (ruling 2) |
| Cabins, decks | not nodes (ruling 3) |
| *Naseby* / *Royal Charles* | one node with a note; flag at the 23 May renaming (ruling 5) |
| 30 March | Pepys does not board the *Naseby* (ruling 6) |
| "the Ship tavern", 23 March | a tavern, not a vessel; Pepys did not go in (ruling 7) |

### Still open

- **Section 6 ruling 4** -- "the Swan tavern", 2 March. Stands as `swan_inn`.
- **Section 6 ruling 12** -- whether `navy_office` and the house Pepys moves
  into in July 1660 stay two nodes.
- **README numbering** -- the principle list runs 1-11, 13, 14, 16, with no 12
  and no 15. Both this file and `CLAUDE.md` cite principles by number.
- **6 March and Mrs Jem** -- the day no longer records the visit to her, which
  sits against section 6 ruling 2 placing her at `scott_house` through
  15 March.

---

## 9. Flagged in the 16-31 March 1659/60 draft

67 edges over 16-23 March, 11 new places, 0 errors. Cross-checked against
network4: 193 curated edges for the month against their 191.

**24-31 March carry no edges at all.** Pepys boards the *Swiftsure* on the 23rd
and does not leave her again in March. She falls into the Hope on the 27th and
lies below Gravesend from the 29th, but he changes no node, so under README
13-14 no edge arises; cabins and decks are not nodes; and he does not board the
*Naseby* on the 30th (section 7 ruling 6). **This is the conventions working as
written, but it means the fleet's movement down the Thames leaves no trace in
the network.** Worth knowing before the voyage proper, where weeks pass with
Pepys aboard: if that movement should be visible, the conventions need another
look, because nothing in the current scheme can carry it.

1. **Five nights at Mrs Crisp's.** From 17 to 21 March Pepys sleeps at
   `crisp_house`, "his mother's house by me in Axe Yard" -- his wife gone to
   Huntsmoor and his own house locked up with her holding the keys. Each night
   is modelled, so the run is continuous.
2. **Pepys corrects his own dating, 20-21 March.** The leave-taking of his
   parents is written under the 20th, but the 21st says "which by a mistake I
   have put down yesterday". It is drafted on the 21st. The coach to London
   that carries him there moves with it.
3. **22 March: the leave-takings.** The first draft compressed them; the
   cross-check showed network4 modelling four visits this draft lacked, and on
   re-reading the entry names three places -- Mrs Hunt's, Mr George Montagu's,
   and the Admiralty for the warrant from Mr Blackburne, its Secretary. Added.
   **Kate Sterpin is still unmodelled**: "took leave of Kate Sterpin" gives no
   place, and she may or may not be the Catan of `kate_petit_house`.
4. **"Tony Robins's", 19 March** is drafted as `roberts_whitehall`, the same
   house as "Roberts at Whitehall" on the 13th. network4 keeps them apart as
   two places.
5. **A fourth Chequer.** `chequer_inn_holborn`, where Elizabeth Pepys took the
   coach for Huntsmoor on the 17th, joins `chequers_inn` and
   `exchequer_tavern_charing_cross` at Charing Cross and `chequer_inn_fowlmere`.
6. **Two Pope's Heads.** `popes_head_tavern_chancery_lane` (22 March) is
   distinct from `popes_head_alley` in the City (7 March).
7. **"my Lord" on 22 March.** "So to my Lord ... where I lay all night with
   Mr. Andrews" is unqualified, so section 6 ruling 1 sends it to
   `sandwich_lodgings` -- though Mr Andrews is met at Mr Crew's elsewhere, and
   network4 reads it as Mr Crew's.
8. **20 March, the flood.** "the water was so high that there was boats rowed
   in King Street and all our yard was drowned, that one could not go to my
   house". He goes to Westminster but cannot reach Axe Yard;
   `westminster_hall` stands in for the Westminster leg.
9. **Named watermen.** 19 March gives the first clean case of README principle
   16: "I got Crockford to carry me over it", so Crockford is a companion and
   the mode is `boat`.
10. **Unnamed stops.** `alehouse_unknown_11` (Drury Lane, 18 March) and
    `tavern_unknown_1` ("a tavern over against Mr. Pierce's", 21 March). The
    Drury Lane alehouse is a separate occasion from `alehouse_unknown_9` on
    3 March, per section 5 ruling 6; network4 reuses one node for both.
11. **April must open aboard.** 23 March ends on `the_swiftsure` and no later
    March day moves, so whatever is drafted next has to depart from her.

---

## 10. From the 16-23 March review, 2 November 2026

### Applied

- **"my Lord's" is now dated within March.** The review moved 17-21 March from
  `sandwich_lodgings` to `john_crews_house`, leaving 22 March ("my Lord's
  lodging **at the gate**") and 23 March at `sandwich_lodgings`. That reads as
  my Lord staying at Mr Crew's until about the 21st and back in his own
  Whitehall lodgings for the departure, which refines section 6 ruling 1 rather
  than reversing it. Section 2 records the dates.
- **Three node renames completed.** `crisp_house` ->
  `crisp_house_axe_yard`, `jervas_barber` -> `richard_jervas_barber`,
  `blagrave_house` -> `thomas_blagrave_house`. Each was renamed on some edges
  and not others, which would have left two ids for one house.
- **"Tony Robins's" is a separate house after all.** The review renamed only
  the 19 March references, leaving 13 March's `roberts_whitehall` alone, so
  `anthony_robins_whitehall` is now its own node -- which is how network4 reads
  it, and what section 9 flag 4 asked.
- **One companion spelling normalised**: "Edward Sheply" (1) to "Edward
  Shipley" (7), which is the spelling in `sandwich_lodgings`'s own note.

### Seven companion near-misses for the team

`validate.py` now compares companion names pairwise and reports close ones,
because folding by case and plural missed "Edward Sheply" beside "Edward
Shipley". It ignores a differing honorific, since "Mr Sheply" and "Mrs Sheply"
are two people. That turned up seven pairs already in the data, none of them
touched:

| | likely |
|---|---|
| `Jemima Montagu` / `Jemimah Montagu` | one person, two spellings |
| `John Hawley` / `John Hawly` | one person |
| `Mr Hawley` / `Mr Hawly` | one person, same man as above |
| `Matthew Lock` / `Matthew Locke` | one person |
| `Mr Shepley` / `Mr Sheply` | one person |
| `William Simons` / `William Symons` | one person |
| `William Howe` / `William Howell` | **probably two different people** |

Choosing the canonical spelling for each is the team's call, as is whether the
bare `Mr Hawly` / `Mr Shepley` forms should become the full names used
elsewhere.

### Two identifications made for one day only

The review named people the draft had left as honorifics, but only on the day
it was reviewing:

- **"Mr Thomas" (7 edges) / "Thomas Crew" (2)** -- named on 23 March as John
  Crew's son. If that holds for 1, 2 and 7 March too, the other five should
  follow.
- **"Mr Woodfine" (2) / "Thomas Woodfine" (1)** -- named on 18 March.

Not propagated, since extending an identification across dates is a
curatorial judgement.

---

## 11. Flagged in the April 1660 draft

10 edges over 4 days, 7 new places, 0 errors across 200 nodes and 799 edges.
April is wholly New Style, the year having turned on 25 March.

**26 of the 30 days carry no edges.** Pepys moves into the *Naseby* on the 2nd
and, apart from visits to three other ships and one afternoon ashore at Deal,
never leaves the ship he is on. The fleet sails from Long Reach to Lee roads on
the 5th, past the Spitts on the 6th, the Nore and South Forelands on the 9th,
and anchors at the Castles about Deal -- none of which is Pepys changing node,
so none of it is an edge. **network4 read the same month independently and got
9 edges over the same 4 days**, which is about as good a corroboration of the
zero-edge days as the method allows.

That makes the shipboard blindness raised in section 9 concrete: the voyage runs
to 8 June, and on current conventions those weeks are nearly empty. The question
is not whether the drafting is right -- it follows the rules -- but whether the
rules should let the fleet's movement be recorded at all.

1. **`london` collides with `city_of_london`.** README 14 gives a ship the
   vessel's name with no suffix, which for the *London* (visited 24 April)
   yields `london` -- which any reader will take for the city. network4 names
   its vessels `london_ship`, `speaker_ship`, `assistance_ship`, and the
   retracted October ruling proposed `naseby_ship` too. Drafted per the README
   as it stands. **Two independent reasons to reconsider the no-suffix rule.**
2. **3 April: an aborted landing, not modelled.** "my Lord went on shore, and
   after him I and Capt. Sparling went in his boat, but the water being almost
   at low water we could not stay for fear of not getting into our boat again.
   So back again." Whether Pepys set foot ashore is unclear and no place is
   named, so no edge was drafted. If it counts, it needs a node for an unnamed
   shore.
3. **`deal` as a shore node, 30 April.** "we took boat and first went on shore,
   it being very pleasant in the fields; but a very pitiful town Deal is", then
   Fuller's and Poole's. network4 goes straight from the boat to Fuller's. The
   extra node is the one edge by which this draft exceeds theirs.
4. **"the Captain", 24 April** -- "with the Captain on board our own ship" read
   as Captain Cuttance, the *Naseby*'s own captain, named elsewhere in the
   month.
5. **The *Naseby* is renamed the *Royal Charles* on 23 May.** One node with a
   note, per section 7 ruling 5. Flagging here so May's draft handles it
   deliberately.
6. **Everyone else moves and Pepys does not.** Shipley goes to Sheppy on the
   7th, Stayner and others to Dover on the 18th, Burr ashore on the 19th,
   Pickering and Balty away on the 9th. None generates an edge, since the
   network records Pepys's movements. Worth confirming that is intended for the
   voyage, where his people are often the ones travelling.
7. **Within-ship places named and not modelled**, per section 7 ruling 3: the
   Round-house (10th), the coach (10th and 21st), the great cabin below, the
   half-deck table (20th), the Lieutenant's cabin, my Lord's storeroom of wine
   (26th).

---

## 12. Ship nodes take a `the_` prefix (2 November 2026)

Every ship node is now `the_` plus the vessel's name:

| was | now |
|---|---|
| `swiftsure` | `the_swiftsure` |
| `naseby` | `the_naseby` |
| `london` | `the_london` |
| `speaker` | `the_speaker` |
| `assistance` | `the_assistance` |

15 edge references and 5 crosswalk rows followed. This settles section 11
flag 1: `the_london` can no longer be mistaken for `city_of_london`, which was
the only real objection to the bare names.

README principle 14 now reads "e.g. the_naseby", so the README, this file and
`CLAUDE.md` agree.

Note also that the prefix is not a reliable marker of a ship: `the_sun_tavern`,
`the_half_moon_alehouse`, `the_swan_pub` and `the_temple` all carry it and none
is a vessel. A ship is identified by its node row, not by its id.


## 13. Flagged in the May 1660 draft

67 edges over 11 days, 33 new nodes, 0 errors. May is the largest chunk so far
by a wide margin — the fleet lies off Scheveling for a fortnight, Pepys goes
ashore in Holland five times, and the King is carried to Dover. The
cross-check against network4 is unusually close: 63 edges over the same 11
days, and every remaining difference is either my draft being finer-grained or
one over-identification on their side (flag 6).

### 1. Three ships the diary will not name

On 3 May Pepys visits most of the fleet. Two vessels are named outright, so
`the_plymouth` and `the_essex` are safe. The rest are not:

- Sir Richard Stayner's ship, where the commanders dined — "took all the
  Commanders and myself on board him to dinner". Drafted as `ship_unknown_1`.
- "After dinner, to the rest of the ships ... quite through the fleet." Visits
  to an unnamed and uncountable number of vessels. I have drafted **only** the
  Assistance, which the entry does name ("staid at the Assistance to hear the
  harper a good while"), and dropped the rest. The day is therefore an
  undercount by construction.

On 22 May the same ship recurs: "the Dukes and my Lord to see the Vice and
Rear-Admirals; and I in a boat after them." The Vice-Admiral's ship is
identifiable as the London from 24 April ("we were on board the London, which
hath a state-room much bigger than the Nazeby"). The Rear-Admiral's is not
named anywhere, so it is `ship_unknown_1` again, on the reading that Stayner
is the Rear-Admiral. **If that reading is wrong, both 3 May and 22 May are
wrong together**, which is the risk of folding them into one node.

The alternative is a separate `ship_unknown_n` per occasion, which loses the
(probable) identity. I have taken identity over caution and flagged it here.

### 2. Five nights ashore in Holland

14-19 May is the first sustained run of nights off the ship since Pepys
embarked. He sleeps ashore on the 14th, 17th, 18th and 19th, and the entries
call the place only "our lodging" — "the Judge and I to another house ... he
and I lay in one press bed" (14th), "After that to our lodging where W. Howe
and I exceeding troubled" (18th). I have drafted one node,
`lodging_unknown_1`, for all four nights.

The 14th and the 17th-19th are separated by two nights aboard (the 15th and
16th), so treating them as the same lodging is an inference, not a statement.
It is a reasonable one — "our lodging" on the 18th implies a standing
arrangement — but if the GRA prefers it split, the second stay needs
`lodging_unknown_2` and the continuity on 17 and 20 May re-pointed.

### 3. Ten unnamed places of new types

May needs more `_unknown_` nodes than every previous month put together,
because Pepys records Dutch places by what they were rather than what they
were called: `eating_house_unknown_1`, `bookshop_unknown_1`,
`tavern_unknown_2` (Scheveling, "a house of entertainment"),
`tavern_unknown_3` (the Hague, flag 4), `house_unknown_1` (the shell-work
woman's), `picture_shop_unknown_1`, `barber_unknown_1`,
`drinking_house_unknown_1` (Lausdune), `dutch_house_unknown_1`, and
`cliff_unknown_1` (flag 5).

Two notes on what I did **not** create. On 19 May "out to buy some linen to
wear against to-morrow, and so to the barber's" gives the barber a place but
the linen shop none, so there is no linen-shop node and no edge for it. On 20
May "I went to lie down in a chamber in the house" at Scheveling is folded
into `scheveling` rather than given a chamber node, per the no-cabin-or-deck
rule read across to rooms generally.

### 4. "the Dr.'s" on 17 May

"going to see the Queen of Bohemia, I met with Dr. Fullers whom I sent to a
tavern with Mr. Edw. Pickering, while I and the rest went to see the Queen ...
After that to the Dr.'s, where we drank a while or so."

I have read "the Dr.'s" as the tavern he had just sent Dr Fuller to, and so
drafted one node (`tavern_unknown_3`) reached once. It could instead be Dr
Fuller's own lodging, or Dr Cade's — Cade appears in the next sentence
supplying the coach. If it is a lodging rather than the tavern, the node's
type and name are wrong, though the edge count does not change. Manually checked by GRA.

### 5. The cliff on 29 May is not Dover

network4 calls it `dover_cliff`. The entry never mentions Dover, and three
details point north of it: the barge lay at Deal and Deal is passed on the way
back ("From thence toward the barge again, and in our way found the people at
Deal"), the fleet is visible from the top, and the cliff measures "not above
thirty-five yards high" — about a third of the Dover cliffs. I have drafted
`cliff_unknown_1`, located "Between Deal and the South Foreland". The landing
place itself is unnamed and I have taken it as Deal, which is the other half of
this flag. Rename to cliff_unknown_deal.

### 6. The 22 May Rear-Admiral's ship: a disagreement with network4

network4 identifies it as `the_speaker`. The diary rules this out: on 25 April
"Dined to-day with Captain Clerke on board the Speaker (a very brave ship)
where was the Vice-Admiral, Rear-Admiral, and many other commanders" — both
admirals are *guests* aboard Captain Clerke's ship. I have not followed
network4 here.

### 7. The boat that never landed, 22 May

"they made to the shore in the Dutch boat that brought them, and I got into
the boat with them ... When we came near the shore, my Lord left them and came
into his own boat, and General Pen and I with him." Pepys gets into a boat,
travels towards the shore, and returns without touching land. Per the April
ruling on the aborted landing there is no edge, and a note on the
`ship_unknown_1` -> `the_naseby` leg records it. This is the second instance;
if the rule is to hold, it is worth promoting from a per-chunk note to section
1. Manually checked by GRA. 

### 8. Two ships renamed on 23 May

"the King and Duke altered the name of some of the ships, viz. the Nazeby into
Charles; the Richard, James; the Speakers Mary" — and six more. Per section 7
ruling 5 each stays one node with a note, so `the_naseby` and `the_speaker`
both now carry their new names in `notes`. Note the diary says **Charles**, not
*Royal Charles*; she is renamed again later, which this ruling will have to
absorb a second time. 

Pepys himself does not move on the 23rd — "My Lord, Mr. Crew, and others, go
on shore to meet the King", not Pepys — so the day has no edges despite being
the most eventful of the month.

### 9. Twenty days with no movement at all

1, 2, 4, 5, 7-13, 16, 21, 23, 24, 26-28, 30 and 31 May produce nothing. That
is 20 of 31 days, and it continues the problem raised in sections 9 and 11
rather than being new: the conventions make the voyage itself invisible. The
fleet crosses from the Downs to Holland and back with the King aboard, and
because a named ship is one location however far she sails, none of it is an
edge. May at least has the Holland excursions to record; March 24-31 produced
zero edges and April ten. This is correct. 

**This is still the open question, and it is now three chunks old.** It is not
a drafting problem — it is whether the rules should permit fleet movement to be
recorded at all. June ends the voyage on the 8th, so if the answer is yes, June
is the last chunk where it matters for 1660. Continue with the current conventions.

### 10. Still open from earlier chunks

- The README's principle numbering runs 1-11, 13, 14, 16. There is no 12 and
  no 15, and both this file and `CLAUDE.md` cite principles by number. The README's principles have been manually renumbered by the GRA.
- Whether `navy_office` and the July 1660 house stay two nodes (section 6
  flag 12).
- Whether the "Mr Thomas"/"Thomas Crew" and "Mr Woodfine"/"Thomas Woodfine"
  identifications propagate back to earlier dates.
- 6 March no longer records the Mrs Jem visit, which conflicts with the
  section 6 ruling 2. Manually checked by GRA.

## 14. The nodes schema splits notes, evidence and variants (7 November 2026)

Ruled after the coordinate pass of 7 November overwrote the `notes` field on
eight nodes, replacing the diary passages that warranted their identifications
with locational description. `st_pauls_cathedral` lost "At Paul's I light ... I
found Dr. Reynolds in the pulpit, and General Monk there"; `ware_hertfordshire`
and `puckeridge_hertfordshire` were emptied outright; `three_tuns_tavern` lost
the variant spelling "the 3 Tun tavern".

That was not a mistake to be reverted — it showed the column was carrying two
jobs that pull in opposite directions. `notes` has to be free for the GRA to
rewrite while placing coordinates; the warrant for an identification has to be
stable. So `nodes.csv` now has eight columns:

```
id,name,variants,location,latitude,longitude,notes,evidence
```

| column | holds | whose |
|---|---|---|
| `evidence` | the diary passage justifying the identification, quoted, with its date | Claude drafts, GRA verifies |
| `notes` | locational and curatorial gloss, to support the coordinate work | **GRA owns and rewrites freely** |
| `variants` | the diary's other spellings for this same place, `; `-separated | Claude drafts, GRA rules |

Nothing is lost in the move: all 106 quotations, the eight overwritten ones
recovered from commit `dd45803`, are now in `evidence`. The non-quotation prose
stayed in `notes`.

### Why `variants` is a column and not a habit

Variant spellings have been the one recurring source of duplicate nodes across
every chunk so far, and finding them has depended on remembering to look.
`validate.py` now checks each node's `name` and `id` against every recorded
variant and warns on a match, and errors if one spelling is claimed by two
nodes. Eleven are recorded so far, the load-bearing ones being:

- `three_tuns_tavern` — "the 3 Tun tavern"
- `john_layton_apothecary` — "Mr Laxton's" (Laxton against Layton)
- `stephens_chamber_temple` — "Mr Stevens" (Stevens against Stephens)
- `anthony_robins_whitehall` — "Tony Robins's", "Roberts at Whitehall"
- `the_naseby` — "the Nazeby" (the diary's usual spelling), "the Charles"
- `the_plymouth` — "the Plimouth"

The check paid for itself immediately by flagging `chequer_inn_holborn` against
`chequers_inn`. That one was a false positive of my own making — I had recorded
"the Chequers" as a variant of `chequers_inn`, which merely restates its name —
and the validator's own "just repeats the name" warning caught it. Three such
empty variants were dropped. **Note for anyone adding to this column: a variant
that restates the name is worse than no variant, because it manufactures
collisions.** The four Chequers (Charing Cross, Holborn, Fowlmere, and the
Exchequer Tavern) are genuinely four places and all remain distinct.

### Open

- Only 11 of 234 nodes have variants. The column should be filled as chunks are
  re-read, not in one pass, and the ones above came from quotations that
  happened to be in `notes` already — earlier chunks were drafted before the
  column existed and will have more.
- `notes` still carries some curatorial warnings that are not locational
  ("kept distinct from chequers_inn", "A fourth Chequer, distinct from ..."). By
  the ruling these sit in a field the GRA rewrites freely, so they are at risk.
  If they should be stable, they want a home in `evidence` or a column of their
  own — say which and I will move them. Do not write in the 'notes' column, only GRA writes in 'notes'. 
