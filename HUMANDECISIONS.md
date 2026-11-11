# Human decisions

**The GRA's file.** Everything here is a decision only a person can make: a
historical judgement, a curatorial convention, or a ruling on an ambiguity the
diary does not resolve. Claude reads this file before drafting and applies what
it says; Claude does not add rulings to it.

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

# D. Answered, for the record

Questions that were live and are now shut. Full reasoning in `DECISIONS.md`.

| Question | Ruling |
|---|---|
| Should fleet movement be recordable? | **No.** Continue with the current conventions. *(10 Nov 2026)* |
| Mrs Jem's location in February | `scott_house`, not `sandwich_lodgings`. Extended to Mrs Ann. |
| Mrs Ann as a separate node | No, unless she travels with Pepys as a companion. |
| How finely to divide the Temple | Keep them separate; precise where named, area-level where not. |
| "the Exchequer at Charing Cross" and "the Chequers" | Two houses, not one. |
| `downings_counsellor_chamber` | Merged into `stephens_chamber_temple`. |
| Unnamed drinking stops | Accept the inference; each occasion its own node. |
| Out-of-order narration | Draft on the sequence described, not the order narrated. |
| `house_of_commons` | Retired. |
| Edge ids | Contiguous, superseding the stable-key rule. |
| `peter_gunning_church` | Retired into `exeter_house_chapel`. |
| `the_new_market` and `market_unknown_1` | Do not overlap. |
| Shared coordinates between nodes | Intended behaviour. |
| Role descriptors as companions | Keep them. |
| Ship node naming | `the_` prefix, settled 2 Nov 2026. |
| "the Swan tavern", 2 March | A separate house: `swan_tavern_king_st`. Applied 7 Nov 2026; the other 20 `swan_inn` legs untouched. |
| Shott's, 8 March | A separate shop: `shotts_woodmonger_whitehall`. |
| "my Lord's" in early March | Unqualified to `sandwich_lodgings`; explicit "at Mr. Crew's" to `john_crews_house`. Refined for 17–21 March. |
| Mr Moore's dinner, 19 February | Stands as `john_crews_house`. |
| "my partner", 20 February | Stands as the descriptor "Pepys's office partner". |
| "the Dr.'s", 17 May | Dr Fuller's lodging: `thomas_fuller_lodging`. |
| The cliff of 29 May | `cliff_unknown_deal`. |
