# Claude decisions

**Claude's file.** How a chunk gets drafted: the method, the defaults applied
when the diary is silent, the readings taken and why, and the corrections made
to earlier work. None of it is authoritative — anything here can be overruled
by `HUMANDECISIONS.md`, which is the GRA's file and wins every time.

The point of keeping it separate is that the GRA should not have to read
Claude's reasoning to find out what has been decided, and Claude should not
quietly promote its own reading into a ruling. A judgement recorded here is a
judgement **awaiting** a ruling; the ruling, when it comes, goes in
`HUMANDECISIONS.md` section A or B.

`DECISIONS.md` is the closed record up to 11 November 2026 and is no longer
added to.

---

## 1. How a chunk is drafted

1. **Read `HUMANDECISIONS.md`.** Apply what is settled; do not re-litigate it.
   If a case is not covered, draft the most defensible reading and flag it
   rather than deciding silently.
2. **Read `README.md` in full** — see section 6 on its numbering.
3. **Search `nodes.csv` before inventing a node**, across `name`, `id` *and*
   `variants`. Variant spellings and honorific differences are the main source
   of accidental duplicates.
4. **Read every entry in the chunk** before drafting any of it. Movement in one
   entry is frequently only resolvable from the next — where Pepys slept is
   often stated the following morning.
5. **Draft** as a script: a node list and a day-keyed table of legs, so the
   whole chunk is regenerable rather than hand-edited.
6. **Validate to zero errors.** This is the bar; a chunk is not drafted until
   it passes.
7. **Cross-check** against the first-generation networks with
   `diff_firstgen.py`, and read every day it reports.
8. **Flag** everything that was a judgement call, into `HUMANDECISIONS.md`
   section A.
9. **Regenerate** the worksheet and workbooks, verify the round-trip is
   lossless, commit.

### What the cross-check is for

It is not a scoring exercise against network4. It is a second reader with no
access to this draft's assumptions, and its value is entirely in the days where
the two disagree. Three outcomes, all useful:

- **network4 is right.** It has happened twice and both were substantive — see
  section 5.
- **This draft is right.** Then the disagreement is worth recording, because an
  independent reader found the passage ambiguous.
- **Both are defensible.** Then it is a ruling for the GRA, not a choice to
  make quietly.

A near-equal edge count across a month is weak evidence of anything. A day where
both drafts agree on an unobvious reading is strong evidence.

---

## 2. Defaults applied when the diary is silent

The diary very often does not say how Pepys travelled, whether he went home, or
what a place was called. These are the standing answers, so the same silence is
not resolved two different ways in two different months.

| Silence | Default |
|---|---|
| No mode given | `walk`. Used for most London legs. |
| No mode given, but the trip is between two Thames landings | `boat`, on geography, and flagged. |
| A day ends somewhere other than where the next begins | Add a closing leg to the last known lodging, note it on the edge as inferred, and flag it. The continuity rule requires the day to close; it does not license silence about the inference. |
| A place is visited but unnamed | A `<type>_unknown_<n>` node, with the quotation as its evidence. Not folded into the preceding node. |
| A sentence narrates out of order | Draft on the sequence described, not the order the text presents it in. |
| Someone is met at the destination | Not a companion. |
| A named vessel sails with Pepys aboard | No edge. He changes no node. |
| A boat sets out but no one lands | No edge, with the attempt noted on the surrounding leg. |
| A room inside a lodging is named | Folded into the lodging. A gallery or chamber that is a public part of a palace gets its own node. *(These two are inconsistent — flagged.)* |

### On inventing nodes

The test is whether the diary places Pepys somewhere, not whether it names the
place. "we went to a place we had taken to sup in" is a node; "the people at
Deal going to make a bonfire" is not, because he passes rather than stops.

An unnamed place gets a node of its own rather than being merged into a
neighbouring one, per the standing ruling. The cost is a growing `_unknown_`
series — May 1660 alone added ten — and that cost is real but visible, which is
better than quietly losing the stop.

---

## 3. Readings taken, by chunk

Only the ones where the text genuinely admitted more than one answer. Each is
flagged in `HUMANDECISIONS.md` section A until ruled on.

### The voyage, March–June 1660

- **Shipboard silence.** 24–31 March, 26 days of April, 20 of May and 1–7 June
  produce no edges. This was raised three times as a possible defect in the
  conventions before being ruled correct. It is recorded here because the
  reasoning matters for later voyages: the rules make the *fleet's* movement
  invisible while recording Pepys's faithfully, and those are different things.
- **Unnamed ships.** Stayner's ship on 3 May and the Rear-Admiral's on 22 May
  were drafted as one node, choosing identity over caution — so both days were
  right or wrong together. The review split them, creating `dutch_ship_unknown`.
  The review's caution was the better call.
- **"the rest of the ships ... quite through the fleet"** (3 May) is an
  uncountable number of visits. Only the Assistance, which the entry names, was
  drafted. The day is an undercount by construction.
- **Nights ashore in Holland**, 14–19 May, were folded into one
  `lodging_unknown_1` on the strength of "**our** lodging" on the 18th, though
  two nights aboard separate the stays.

### London, June 1660

- **Where my Lord lodged** — see section 5, a correction rather than a reading.
- **The ride up from Deal, 8 June** is a telegraphic list. Rochester and Chatham
  are drafted in road order against the order the entry names them, because the
  road from Sittingbourne to Gravesend passes Chatham first. network4 merged the
  two into one node, which avoids the question rather than answering it.
- **Three unqualified house names** — a Sun, a Leg, a Bell — were each resolved
  to the nearest candidate already in the data. All three are guesses and all
  three are flagged.
- **The Exchequer at Charing Cross is the King's Head.** 20 June's "now the
  King's Head Tavern" reads as a Restoration renaming of a house already in the
  data, so it was recorded as a `variants` entry rather than drafted as a fifth
  Charing Cross tavern. This is the case the `variants` column exists for.

---

## 4. Tooling decisions

The validator is where a convention becomes enforceable. Checks are added when
a class of error gets through review, not speculatively.

| Check | Added because |
|---|---|
| Edge endpoints must exist in `nodes.csv`, with "did you mean" suggestions | Human review renamed ids in the edges and not the nodes **five separate times**. This is the single most common breakage in the project. |
| Crosswalk staleness | Same cause: a rename leaves the crosswalk pointing at a retired id. |
| Companion near-misses, fuzzy-matched, honorific-aware | "Edward Sheply" sat beside "Edward Shipley" undetected. Honorifics are compared first, since "Mr Sheply" and "Mrs Sheply" are two people. |
| Variants cross-referenced against every node's `name` and `id` | Variant spellings are the main duplicate risk. It caught a real collision on its first run — which turned out to be a redundant variant Claude had added, so the check also warns when a variant merely restates its node's name. |
| Quotations left in `notes` | After the column split, a warrant in `notes` is a warrant that will be overwritten. |
| Whitespace in text fields | The `.xlsx` round-trip silently normalises a trailing space, which broke losslessness once. |
| Old Style year against each date | Mechanical and easy to get wrong at the 25 March boundary. |
| `_unknown_` numbering contiguity | Gaps and repeats accumulate invisibly across months. |

**On the diary parser.** `diary.py` originally matched only `1st`/`2nd`-style
day headings and silently dropped 16–20% of the corpus — 564 entries. Entries
headed `2d.`, `February 1st.`, `5th,(Lord's day).`, `31st Office day.` and the
combined `8th, 9th, Loth, 11th, 12th, 13th.` all failed. The lesson worth
keeping: a parser that drops input silently is worse than one that crashes, and
the only way this surfaced was counting what came out against what went in.

---

## 5. Corrections to earlier work

Kept in full. A correction that is edited away teaches nothing, and three of
these were caught by other readers rather than by Claude.

### Where my Lord lodged, June 1660 — caught by the cross-check

Every "to my Lord" was drafted to `sandwich_lodgings`, his Whitehall rooms.
network4 sent them to Mr Crew's house and was right. Three things settle it:
25 June, "this being the first night of his coming to Whitehall **to lie**
since his coming from sea"; 19 June, "towards my Lord's **at Mr. Crew's**"; and
on 11, 16 and 22 June Pepys goes "to my Lord" and *then* "to White Hall with
him", so my Lord cannot have been at Whitehall already.

Sixteen visits were re-pointed. The repair had to be done per **visit** rather
than per endpoint — the first attempt rewrote one leg's source without its
predecessor's target and created a self-loop.

### The README principles — my error, repeated across four sections

I reported four times that `README.md` was missing principles 6, 12 and 15 and
that its numbering was "broken". It is not: Markdown ordered lists renumber on
render, honouring only the first number, so a source reading
`1 2 3 4 5 7 8 9 10 11 13 14 16` displays as a consecutive **1–13**. Thirteen
principles, complete and in order.

I had read the list with `grep` over the raw source — precisely where the
artefact lives and where a human never looks. **When a convention is about how a
document presents itself, reading the bytes is not reading the document.**

What is real: source and rendered numbering agree for the first five principles
and diverge after. Source 14 (ships) renders as 12; source 10 (precision inside
a complex) renders as 9. This project cites **source** numbers — every citation
was checked against its principle's text and all resolve correctly, including
the GRA's own "README principle 14". The hazard runs the other way: someone
looking up "principle 10" in the rendered file finds a different rule. So quote
the words alongside the number.

### A GitHub access diagnosis, reported as fixed before it was

A push failed with 403. I reported it resolved on the strength of a successful
`list_branches` call — which had succeeded through a different credential, as
public read. The actual cause was that the repository was not in the GitHub
App's selected-repositories list. **A read succeeding does not mean a write
will.**

### Smaller ones

- **8 March, the Commons lobby.** The draft had Pepys entering; "sending a note
  to my Lord, **he comes out to me**" says he never did. Caught in review.
- **22 March, the leave-takings** were compressed into fewer legs than the entry
  supports. The cross-check showed network4 modelling four visits this draft
  lacked; re-reading, three had named places. The day grew from 8 edges to 11.
- **The `slug_words` cross-check bug.** Identifiers were compared as
  concatenated strings, so `bridge_tavern` matched inside "Cam**bridge**" and
  every Cambridge college mapped to the Bridge Tavern. Fixed to compare word
  sets.
- **A redundant variant.** `"the Chequers"` was recorded as a variant of
  `chequers_inn`, which merely restates its name, and promptly produced a false
  duplicate warning against `chequer_inn_holborn`. Three such variants were
  dropped. A variant that restates the name is worse than none.

---

## 6. Reading `README.md`

The principles are complete. Source numbering and rendered numbering diverge
from the sixth principle on:

| source | rendered | principle |
|---|---|---|
| 1–5 | 1–5 | *(identical)* |
| 7 | 6 | most specific label for a person |
| 8 | 7 | honorific when no first name |
| 9 | 8 | honorific on a person's home |
| 10 | 9 | precision inside a sprawling complex |
| 11 | 10 | area-level labels for semi-known places |
| 13 | 11 | a named ship is one location |
| 14 | 12 | ship nodes take the vessel's name |
| 16 | 13 | named watermen and coachmen as companions |

Cite the source numbers, and quote the principle's words alongside.
