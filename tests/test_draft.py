import unittest

from heddle.draft import draft, odd_plain_warning, plain_tie_up, twill_tie_up
from heddle.format import format_plan
from heddle.plan import PlanError, plan_warp


def project(**overrides):
    base = {
        "name": "Sample scarf",
        "yarn": "8/2 cotton",
        "widthIn": 10,
        "epi": 24,
        "lengthIn": 72,
        "loomWasteIn": 27,
        "shafts": 4,
    }
    base.update(overrides)
    return base


class DraftTests(unittest.TestCase):
    def test_plain_and_twill_tie_ups(self):
        self.assertEqual(plain_tie_up(4), [[1, 3], [2, 4]])
        self.assertEqual(plain_tie_up(2), [[1], [2]])
        self.assertEqual(twill_tie_up(4), [[1, 2], [2, 3], [3, 4], [4, 1]])

    def test_default_weave_is_plain(self):
        plan = plan_warp(project())
        self.assertEqual(plan["draft"]["weave"], "plain")
        self.assertEqual(plan["draft"]["treadling"], [1, 2])
        self.assertEqual(plan["draft"]["lifts"], [[1, 3], [2, 4]])
        text = format_plan(plan)
        self.assertIn("weave: plain", text)
        self.assertIn("treadle 1: 1 3", text)
        self.assertIn("pick 2: 2 4", text)

    def test_twill_needs_four_shafts(self):
        plan = plan_warp(project(weave="twill"))
        self.assertEqual(plan["draft"], draft(4, "twill"))
        with self.assertRaises(PlanError) as caught:
            plan_warp(project(shafts=2, weave="twill"))
        self.assertIn("weave:", str(caught.exception))
        with self.assertRaises(PlanError):
            plan_warp(project(weave="satin"))

    def test_odd_shafts_warn_for_plain_weave(self):
        self.assertIsNone(odd_plain_warning(4, "plain"))
        self.assertIn("neighboring", odd_plain_warning(3, "plain"))
        plan = plan_warp(project(shafts=3, widthIn=1, epi=3))
        self.assertTrue(any("neighboring" in item for item in plan["warnings"]))


if __name__ == "__main__":
    unittest.main()
