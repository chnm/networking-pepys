"""Split the diary text files into per-day entries.

Month headers sit at the start of a line ("JANUARY 1659-1660", "APRIL 1660")
and each day begins "1st." / "22nd." / "13th." at the start of a line. The
first entry of a month is sometimes unlabelled, in which case the text between
the header and the next day marker is taken as day 1.
"""
import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YEARS = os.path.join(REPO, "years")

MONTHS = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY",
          "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
MONTH_RE = re.compile(r"^(%s)\s+16\d\d(?:[-/]\d+)?\s*$" % "|".join(MONTHS), re.M)
DAY_RE = re.compile(r"^(\d{1,2})(?:st|nd|rd|th)\.", re.M)


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
            if lead and int(marks[0].group(1)) != 1:
                out[(mon, 1)] = lead
        for j, m in enumerate(marks):
            stop = marks[j + 1].start() if j + 1 < len(marks) else len(body)
            day = int(m.group(1))
            chunk = body[m.start():stop].strip()
            # A repeated day number means a continued entry, not a new one.
            if (mon, day) in out:
                out[(mon, day)] += "\n\n" + chunk
            else:
                out[(mon, day)] = chunk
    return out


def flow(entry):
    """Rewrap an entry into paragraphs with single-spaced lines."""
    paras = re.split(r"\n\s*\n", entry)
    return [" ".join(p.split()) for p in paras if p.strip()]
