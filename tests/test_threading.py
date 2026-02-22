import unittest

from heddle.format import format_plan
from heddle.plan import PlanError, plan_warp
from heddle.threading import point_repeat, straight_repeat, thread_ends


class ThreadingTests(unittest.TestCase):
    def test_repeats(self):
        self.assertEqual(straight_repeat(4), [1, 2, 3, 4])
        self.assertEqual(point_repeat(4), [1, 2, 3, 4, 3, 2])
        self.assertEqual(point_repeat(2), [1, 2])

    def test_full_repeats_and_remainder(self):
        straight = thread_ends(10, 4, "straight")
        self.assertEqual(straight["repeats"], 2)
        self.assertEqual(straight["remainder"], [1, 2])
        point = thread_ends(216, 4, "point")
        self.assertEqual(point["repeats"], 36)
        self.assertEqual(point["remainder"], [])

    def test_plan_defaults_to_straight_and_rejects_other_names(self):
        plan = plan_warp(
            {
                "name": "Sample scarf",
                "yarn": "8/2 cotton",
                "widthIn": 10,
                "epi": 24,
                "lengthIn": 72,
                "loomWasteIn": 27,
                "shafts": 4,
            }
        )
        self.assertEqual(plan["threading"]["kind"], "straight")
        self.assertEqual(plan["threading"]["repeats"], 60)
        text = format_plan(plan)
        self.assertIn("repeat: 1 2 3 4", text)
        self.assertIn("remainder: none", text)
        with self.assertRaises(PlanError) as caught:
            plan_warp({**plan_project(), "threading": "rosepath"})
        self.assertIn("threading:", str(caught.exception))


def plan_project():
    return {
        "name": "Sample scarf",
        "yarn": "8/2 cotton",
        "widthIn": 10,
        "epi": 24,
        "lengthIn": 72,
        "loomWasteIn": 27,
        "shafts": 4,
    }


if __name__ == "__main__":
    unittest.main()
