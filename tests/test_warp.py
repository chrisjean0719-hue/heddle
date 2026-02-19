import unittest

from heddle.warp import end_count, odd_end_warning, pounds, sett_warning, warp_yards
from heddle.yarns import lookup_yarn


class WarpTests(unittest.TestCase):
    def test_scarf_ends_and_yards(self):
        self.assertEqual(end_count(10, 24), 240)
        self.assertAlmostEqual(warp_yards(240, 72, 27), 660)

    def test_half_an_end_rounds_up(self):
        self.assertEqual(end_count(1.05, 10), 11)
        self.assertEqual(end_count(1.02, 10), 10)

    def test_pounds_from_yards(self):
        self.assertAlmostEqual(pounds(660, 3360), 660 / 3360)

    def test_sett_and_odd_ends(self):
        cotton = lookup_yarn("8/2 cotton")
        self.assertIsNone(sett_warning(cotton, 24))
        self.assertIn("outside the plain-weave range", sett_warning(cotton, 30))
        self.assertIsNone(odd_end_warning(240))
        self.assertIn("odd", odd_end_warning(241))


if __name__ == "__main__":
    unittest.main()
