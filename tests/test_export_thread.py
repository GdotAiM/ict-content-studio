from pathlib import Path

import export_thread

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "examples/thread_2026-01-15.md"


def _gate(tmp_path, verdict):
    g = tmp_path / "gate.md"
    g.write_text(f"# Gate\nVERDICT: {verdict}\n", encoding="utf-8")
    return g


def test_exports_when_ships(tmp_path):
    out = tmp_path / "ready"
    rc = export_thread.main(["--file", str(EXAMPLE), "--gate-report", str(_gate(tmp_path, "SHIPS")),
                             "--out-dir", str(out), "--timestamp", "2026-01-15 16:30"])
    assert rc == 0
    f = out / "2026-01-15_1630_thread.md"
    text = f.read_text(encoding="utf-8")
    assert "## Post 1/6" in text and "## Post 6/6" in text
    assert "EXAMPLE THREAD" not in text  # header line stripped


def test_blocked_when_does_not_ship(tmp_path):
    out = tmp_path / "ready"
    rc = export_thread.main(["--file", str(EXAMPLE), "--gate-report", str(_gate(tmp_path, "DOES NOT SHIP")),
                             "--out-dir", str(out)])
    assert rc == 1 and not out.exists()


def test_blocked_on_long_post(tmp_path):
    d = tmp_path / "d.md"
    d.write_text("ok\n---\n" + "z" * 300, encoding="utf-8")
    out = tmp_path / "ready"
    assert export_thread.main(["--file", str(d), "--gate-report", str(_gate(tmp_path, "SHIPS")),
                               "--out-dir", str(out)]) == 1
    assert not out.exists()


def test_blocked_on_banned_phrase(tmp_path):
    d = tmp_path / "d.md"
    d.write_text("This is guaranteed\n---\nfine", encoding="utf-8")
    assert export_thread.main(["--file", str(d), "--gate-report", str(_gate(tmp_path, "SHIPS")),
                               "--out-dir", str(tmp_path / "r")]) == 1


def test_missing_file(tmp_path):
    assert export_thread.main(["--file", str(tmp_path / "no.md"),
                               "--gate-report", str(_gate(tmp_path, "SHIPS"))]) == 2
