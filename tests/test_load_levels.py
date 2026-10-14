import json
from pathlib import Path

import load_levels

ROOT = Path(__file__).resolve().parents[1]
GOOD = """date: 2026-10-14
instrument: CAPITALCOM:US100
source: TradingView manual
time_sast: 13:05
ny_midnight_open: 20125.4
prior_day_high: 20210
prior_day_low: 20,050.5
asia_high: 20150
asia_low: 20100
london_high: 20180
london_low: UNAVAILABLE — needs manual input
equal_highs_lows_notes: EQH ~20210
"""


def test_parse_good(tmp_path, capsys):
    f = tmp_path / "levels_2026-10-14.md"
    f.write_text(GOOD, encoding="utf-8")
    assert load_levels.main([str(f)]) == 0
    d = json.loads(capsys.readouterr().out)
    assert d["prior_day_low"] == 20050.5 and d["london_low"] is None
    assert d["label"] == "CAPITALCOM CFD" and d["instrument"] == "CAPITALCOM:US100"


def test_template_is_invalid_until_filled():
    _, errs = load_levels.parse_text((ROOT / "inputs/levels_TEMPLATE.md").read_text(encoding="utf-8"))
    assert errs


def test_rejects_bad_values():
    bad = GOOD.replace("CAPITALCOM:US100", "NQ1!").replace("20125.4", "abc").replace("13:05", "25:00")
    _, errs = load_levels.parse_text(bad)
    assert len(errs) == 3


def test_rejects_high_below_low():
    _, errs = load_levels.parse_text(GOOD.replace("asia_high: 20150", "asia_high: 20000"))
    assert any("asia_high" in e for e in errs)


def test_missing_field_and_file(tmp_path):
    _, errs = load_levels.parse_text(GOOD.replace("source: TradingView manual\n", ""))
    assert "missing field: source" in errs
    assert load_levels.main([str(tmp_path / "nope.md")]) == 2
