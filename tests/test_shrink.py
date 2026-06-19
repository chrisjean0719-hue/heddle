import unittest

from heddle.format import format_plan
from heddle.plan import PlanError, plan_warp
from heddle.shrink import finished_measure, half_size_warning


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


class ShrinkTests(unittest.TestCase):
    def test_finished_measure_applies_take_up_then_shrinkage(self):
        self.assertAlmostEqual(finished_measure(10, 10, 10), 8.1)
        self.assertAlmostEqual(finished_measure(72, 10, 10), 58.32)

    def test_omitted_rates_leave_the_on_loom_size(self):
        plan = plan_warp(project())
        self.assertEqual(plan["finished"]["width_in"], 10)
        self.assertEqual(plan["finished"]["length_in"], 72)
        text = format_plan(plan)
        self.assertIn("take-up: 0% width, 0% length", text)
        self.assertIn("finished: 10 in wide, 72 in long", text)

    def test_sample_scarf_finished_size(self):
        plan = plan_warp(
            project(takeUp={"width": 10, "length": 10}, shrinkage={"width": 10, "length": 10})
        )
        self.assertAlmostEqual(plan["finished"]["width_in"], 8.1)
        self.assertAlmostEqual(plan["finished"]["length_in"], 58.32)

    def test_rejects_a_full_loss_and_warns_when_half_is_lost(self):
        with self.assertRaises(PlanError) as caught:
            plan_warp(project(shrinkage={"width": 100, "length": 0}))
        self.assertIn("shrinkage.width:", str(caught.exception))
        with self.assertRaises(PlanError):
            plan_warp(project(takeUp=10))
        self.assertIn("half", half_size_warning(10, 1.6, "width"))
        plan = plan_warp(project(takeUp={"width": 60, "length": 0}, shrinkage={"width": 60, "length": 0}))
        self.assertAlmostEqual(plan["finished"]["width_in"], 1.6)
        self.assertTrue(any("finished width" in item for item in plan["warnings"]))
        self.assertFalse(any("finished length" in item for item in plan["warnings"]))


if __name__ == "__main__":
    unittest.main()
