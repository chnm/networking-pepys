"""Split the diary text files into per-day entries.

Month headers sit at the start of a line ("JANUARY 1659-1660", "APRIL 1660")
and each day begins "1st." / "22nd." / "13th." at the start of a line. The
Wheatley text is inconsistent about ordinal suffixes -- "2d." and "3d." appear
alongside "2nd." and "3rd." -- so the bare "d." form is accepted too. The first
entry of a month is sometimes unlabelled, in which case the text between the
header and the next day marker is taken as day 1.
"""
import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YEARS = os.path.join(REPO, "years")

MONTHS = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY",
          "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
MONTH_RE = re.compile(r"^(%s)\s+16\d\d(?:[-/]\d+)?\s*$" % "|".join(MONTHS), re.M)

# A day marker sits at the start of a line and ends in a period, but the
# Wheatley text varies: "1st.", "2d.", "February 1st.", "5th,(Lord's day).",
# "19th (Lord's day).". An optional month word may precede the ordinal and an
# optional parenthetical may sit between the ordinal and the period. Requiring
# that closing period is what keeps wrapped prose ("...the 20th of March...")
# from registering as an entry.
_MONTH_WORD = "|".join(m.title() for m in MONTHS) + "|" + \
    "|".join(m.title()[:3] for m in MONTHS)
_ORD = r"(?:\d{1,2}(?:st|nd|rd|th|d)|Loth)"

# A day marker sits at the start of a line and ends in a period. The Wheatley
# text varies a good deal: "1st.", "2d.", "February 1st.", "5th,(Lord's day).",
# "19th (Lord's day).", and two entries covering several days at once --
# "8th, 9th, Loth, 11th, 12th, 13th." and "16th, 17th, 18th, 19th." (both July
# 1661), where "Loth" is the scan's slip for "10th". Requiring the closing
# period is what stops wrapped prose ("...on the 20th of March...") from
# registering as an entry.
DAY_RE = re.compile(
    r"^(?:(?:%s)\.?\s+)?%s(?:\s*,\s*%s)*\s*,?\s*(?:\([^)]*\)\s*)?\."
    % (_MONTH_WORD, _ORD, _ORD), re.M)
_ORDINAL_RE = re.compile(r"(\d{1,2})(?:st|nd|rd|th|d)|(Loth)")


def days_covered(marker):
    """Every day number named in a (possibly combined) entry marker."""
    return [10 if loth else int(num)
            for num, loth in _ORDINAL_RE.findall(marker)]


def path(year):
    return os.path.join(YEARS, "diary_%s.txt" % year)


def entries(year, month=None):
    """-> {(month, day): entry text}, in diary order."""
    with open(path(year), encoding="utf-8") as fh:
        text = fh.read()

    heads = list(MONTH_RE.finditer(text))
    if not heads:
        raise SystemExit("no month headers found in %s" % path(year))

    out = {}
    for i, h in enumerate(heads):
        mon = MONTHS.index(h.group(1)) + 1
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        body = text[h.end():end]
        if month and mon != month:
            continue

        marks = list(DAY_RE.finditer(body))
        if marks and marks[0].start() > 0:
            lead = body[:marks[0].start()].strip()
            if lead and days_covered(marks[0].group(0))[0] != 1:
                out[(mon, 1)] = lead
        for j, m in enumerate(marks):
            stop = marks[j + 1].start() if j + 1 < len(marks) else len(body)
            chunk = body[m.start():stop].strip()

            days = days_covered(m.group(0))
            for day in days:
                # A repeated day number means a continued entry, not a new one.
                if (mon, day) in out:
                    out[(mon, day)] += "\n\n" + chunk
                else:
                    out[(mon, day)] = chunk
    return out


def combined_days(year):
    """-> {(month, day): [every day sharing that entry]} for combined entries."""
    shared = {}
    for (mon, day), txt in entries(year).items():
        m = DAY_RE.match(txt)
        days = days_covered(m.group(0)) if m else []
        if len(days) > 1:
            shared[(mon, day)] = days
    return shared


def flow(entry):
    """Rewrap an entry into paragraphs with single-spaced lines."""
    paras = re.split(r"\n\s*\n", entry)
    return [" ".join(p.split()) for p in paras if p.strip()]
