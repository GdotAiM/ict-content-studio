#!/usr/bin/env python3
"""Validate and parse inputs/levels_YYYY-MM-DD.md (manual TradingView levels) to JSON.

Exit 0 + JSON on stdout when valid; exit 1 with errors on stderr otherwise; 2 if file missing.
Price fields may be 'UNAVAILABLE — needs manual input' (emitted as null).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

UNAVAILABLE = "UNAVAILABLE — needs manual input"
INSTRUMENT = "CAPITALCOM:US100"
SOURCE = "TradingView manual"
PRICE_FIELDS = ["ny_midnight_open", "prior_day_high", "prior_day_low",
                "asia_high", "asia_low", "london_high", "london_low"]
REQUIRED = ["date", "instrument", "source", "time_sast", *PRICE_FIELDS]
NUM_RE = re.compile(r"^\d+(\.\d+)?$")


def parse_text(text: str) -> tuple[dict, list[str]]:
    raw: dict[str, str] = {}
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith("#") or ":" not in s:
            continue
        k, v = s.split(":", 1)
        raw[k.strip().lower()] = v.strip()
    errors: list[str] = []
    out: dict = {}
    for k in REQUIRED:
        if k not in raw or raw[k] == "":
            errors.append(f"missing field: {k}")
    if errors:
        return {}, errors
    try:
        out["date"] = date.fromisoformat(raw["date"]).isoformat()
    except ValueError:
        errors.append(f"bad date: {raw['date']!r} (want YYYY-MM-DD)")
    if raw["instrument"] != INSTRUMENT:
        errors.append(f"instrument must be {INSTRUMENT}")
    out["instrument"] = raw["instrument"]
    if raw["source"] != SOURCE:
        errors.append(f"source must be '{SOURCE}'")
    out["source"] = raw["source"]
    if not re.fullmatch(r"([01]\d|2[0-3]):[0-5]\d", raw["time_sast"]):
        errors.append(f"bad time_sast: {raw['time_sast']!r} (want HH:MM)")
    out["time_sast"] = raw["time_sast"]
    for k in PRICE_FIELDS:
        v = raw[k].replace(",", "")
        if raw[k] == UNAVAILABLE:
            out[k] = None
        elif NUM_RE.match(v):
            out[k] = float(v)
        else:
            errors.append(f"bad price for {k}: {raw[k]!r}")
    for hi, lo in (("prior_day_high", "prior_day_low"), ("asia_high", "asia_low"), ("london_high", "london_low")):
        if isinstance(out.get(hi), float) and isinstance(out.get(lo), float) and out[hi] < out[lo]:
            errors.append(f"{hi} < {lo}")
    out["equal_highs_lows_notes"] = raw.get("equal_highs_lows_notes", "")
    out["label"] = "CAPITALCOM CFD"
    return (out if not errors else {}), errors


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("file")
    a = ap.parse_args(argv)
    p = Path(a.file)
    if not p.is_file():
        print(f"error: file not found: {p}", file=sys.stderr)
        return 2
    data, errors = parse_text(p.read_text(encoding="utf-8"))
    if errors:
        for e in errors:
            print(f"INVALID: {e}", file=sys.stderr)
        return 1
    print(json.dumps(data, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
