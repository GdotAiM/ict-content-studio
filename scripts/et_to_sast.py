#!/usr/bin/env python3
"""Convert New York (ET) wall-clock times to SAST (Africa/Johannesburg), DST-correct via zoneinfo.

  et_to_sast.py 09:30 [10:00 11:00] [--date 2026-10-14]
Prints e.g. "09:30 ET (EDT) = 15:30 SAST (2026-10-14)". Exit 2 on bad input.
"""
from __future__ import annotations

import argparse
import sys
from datetime import date, datetime, time
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
SAST = ZoneInfo("Africa/Johannesburg")


def et_to_sast(hhmm: str, on: date) -> datetime:
    t = time.fromisoformat(hhmm)
    return datetime.combine(on, t, tzinfo=ET).astimezone(SAST)


def label(hhmm: str, on: date) -> str:
    et = datetime.combine(on, time.fromisoformat(hhmm), tzinfo=ET)
    s = et.astimezone(SAST)
    return f"{et:%H:%M} ET ({et.tzname()}) = {s:%H:%M} SAST ({s:%Y-%m-%d})"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("times", nargs="+", help="HH:MM in New York time")
    ap.add_argument("--date", help="YYYY-MM-DD (ET calendar date); default today in ET")
    args = ap.parse_args(argv)
    try:
        on = date.fromisoformat(args.date) if args.date else datetime.now(ET).date()
        lines = [label(t, on) for t in args.times]
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
