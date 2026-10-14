from datetime import date

import et_to_sast as m


def test_edt():
    assert m.et_to_sast("09:30", date(2026, 10, 14)).strftime("%H:%M") == "15:30"


def test_est():
    assert m.et_to_sast("09:30", date(2026, 1, 15)).strftime("%H:%M") == "16:30"


def test_us_dst_transitions_2026():
    # US DST starts 2026-03-08, ends 2026-11-01
    assert m.et_to_sast("09:30", date(2026, 3, 6)).hour == 16
    assert m.et_to_sast("09:30", date(2026, 3, 9)).hour == 15
    assert m.et_to_sast("09:30", date(2026, 10, 30)).hour == 15
    assert m.et_to_sast("09:30", date(2026, 11, 2)).hour == 16


def test_day_rollover():
    assert m.et_to_sast("20:00", date(2026, 10, 14)).strftime("%Y-%m-%d %H:%M") == "2026-10-15 02:00"


def test_cli(capsys):
    assert m.main(["10:00", "11:00", "--date", "2026-10-14"]) == 0
    out = capsys.readouterr().out
    assert "10:00 ET (EDT) = 16:00 SAST" in out and "11:00 ET (EDT) = 17:00 SAST" in out
    assert m.main(["25:99", "--date", "2026-10-14"]) == 2
