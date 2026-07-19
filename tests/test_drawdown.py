import unittest

from heddle.drawdown import drawdown_rows, drawdown_svg
from heddle.format import format_plan
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
        "threading": "straight",
        "weave": "plain",
    }
    base.update(overrides)
    return base


class DrawdownTests(unittest.TestCase):
    def test_plain_weave_is_a_checkerboard(self):
        rows = drawdown_rows([1, 2, 3, 4], [[1, 3], [2, 4]], repeats=1)
        self.assertEqual(rows, [[True, False, True, False], [False, True, False, True]])

    def test_two_repeats_of_the_scarf(self):
        plan = plan_warp(project())
        self.assertEqual(plan["drawdown"]["ends"], 8)
        self.assertEqual(plan["drawdown"]["picks"], 4)
        self.assertIn("drawdown: 8 ends by 4 picks", format_plan(plan))
        svg = drawdown_svg(plan["name"], plan["drawdown"]["rows"])
        self.assertIn('viewBox="0 0 64 32"', svg)
        self.assertIn('fill="black"', svg)
        self.assertIn('fill="white"', svg)
        self.assertIn("<title>Sample scarf drawdown</title>", svg)

    def test_point_twill_rises_where_the_shaft_is_lifted(self):
        rows = drawdown_rows([1, 2, 3, 4, 3, 2], [[1, 2], [2, 3], [3, 4], [4, 1]], repeats=1)
        self.assertEqual(
            rows[0],
            [True, True, False, False, False, True],
        )
        self.assertEqual(
            rows[3],
            [True, False, False, True, False, False],
        )


if __name__ == "__main__":
    unittest.main()
