import unittest

from heddle.format import format_plan
from heddle.plan import PlanError, plan_warp


SCARF = {
    "name": "Sample scarf",
    "yarn": "8/2 cotton",
    "widthIn": 10,
    "epi": 24,
    "lengthIn": 72,
    "loomWasteIn": 27,
    "shafts": 4,
}


class PlanTests(unittest.TestCase):
    def test_scarf_plan(self):
        plan = plan_warp(SCARF)
        self.assertEqual(plan["ends"], 240)
        self.assertAlmostEqual(plan["yards"], 660)
        self.assertAlmostEqual(plan["pounds"], 660 / 3360)
        self.assertEqual(plan["warnings"], [])
        text = format_plan(plan)
        self.assertIn("Sample scarf", text)
        self.assertIn("ends: 240", text)
        self.assertIn("660 yd", text)
        self.assertIn("12 dents/in, 2 ends per dent", text)
        self.assertNotIn("warning:", text)

    def test_warns_and_rejects(self):
        plan = plan_warp({**SCARF, "widthIn": 10.1, "epi": 30})
        self.assertEqual(plan["ends"], 303)
        self.assertTrue(any("outside the plain-weave range" in item for item in plan["warnings"]))
        self.assertTrue(any("odd" in item for item in plan["warnings"]))
        with self.assertRaises(PlanError) as caught:
            plan_warp({**SCARF, "yarn": "silk"})
        self.assertIn("yarn:", str(caught.exception))


if __name__ == "__main__":
    unittest.main()
