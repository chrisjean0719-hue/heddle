import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CommandTests(unittest.TestCase):
    def test_plan_command(self):
        completed = subprocess.run(
            [sys.executable, "-m", "heddle", "plan", "examples/scarf.json"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("ends: 240", completed.stdout)
        self.assertIn("660 yd", completed.stdout)

    def test_bad_json(self):
        path = ROOT / "examples" / "scarf.json"
        self.assertIn("name", json.loads(path.read_text(encoding="utf-8")))
        completed = subprocess.run(
            [sys.executable, "-m", "heddle"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 2)

    def test_draw_command_writes_svg(self):
        completed = subprocess.run(
            [sys.executable, "-m", "heddle", "draw", "examples/scarf.json"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("<svg ", completed.stdout)
        with tempfile.TemporaryDirectory() as directory:
            written = subprocess.run(
                [sys.executable, "-m", "heddle", "draw", "examples/scarf.json", "--out", directory],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(written.returncode, 0, written.stderr)
            svg = Path(directory) / "drawdown.svg"
            self.assertTrue(svg.is_file())
            self.assertIn("Sample scarf drawdown", svg.read_text(encoding="utf-8"))

    def test_compare_command(self):
        completed = subprocess.run(
            [sys.executable, "-m", "heddle", "compare", "examples/scarf.json", "examples/towel.json"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("ends: 240 vs 216", completed.stdout)
        self.assertIn("finished width: 8.1 in vs 15.39 in", completed.stdout)
        failed = subprocess.run(
            [sys.executable, "-m", "heddle", "compare", "examples/scarf.json", "examples/missing.json"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(failed.returncode, 1)
        self.assertIn("examples/missing.json:", failed.stderr)


if __name__ == "__main__":
    unittest.main()
