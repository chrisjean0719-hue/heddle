import unittest

from heddle.compare import compare_plans, format_compare
from heddle.plan import plan_warp


def project(**overrides):
    base = {
        "name": "Sample scarf",
        "yarn": "8/2 cotton",
        "widthIn": 10,
        "epi": 24,
        "lengthIn": 72,
        "loomWasteIn": 27,
        "shafts": 4,
        "takeUp": {"width": 10, "length": 10},
        "shrinkage": {"width": 10, "length": 10},
    }
    base.update(overrides)
    return base


class CompareTests(unittest.TestCase):
    def test_scarf_against_towel(self):
        scarf = plan_warp(project())
        towel = plan_warp(
            project(
                name="Sample towel",
                yarn="8/4 cotton",
                widthIn=18,
                epi=12,
                lengthIn=36,
                loomWasteIn=24,
                takeUp={"width": 5, "length": 5},
                shrinkage={"width": 10, "length": 15},
            )
        )
        diff = compare_plans(scarf, towel)
        self.assertEqual(diff["ends"], (240, 216))
        self.assertEqual(diff["yards"], (660, 360))
        self.assertAlmostEqual(diff["finished_width_in"][0], 8.1)
        self.assertAlmostEqual(diff["finished_width_in"][1], 15.39)
        text = format_compare(scarf, towel, diff)
        self.assertIn("Sample scarf vs Sample towel", text)
        self.assertIn("ends: 240 vs 216", text)
        self.assertIn("yards: 660 vs 360", text)
        self.assertIn("finished width: 8.1 in vs 15.39 in", text)


if __name__ == "__main__":
    unittest.main()
