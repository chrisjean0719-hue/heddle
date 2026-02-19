import unittest

from heddle.reed import reed_choices


class ReedTests(unittest.TestCase):
    def test_24_epi_uses_whole_dents(self):
        self.assertEqual(
            reed_choices(24),
            [
                {"dents_per_inch": 6, "ends_per_dent": 4},
                {"dents_per_inch": 8, "ends_per_dent": 3},
                {"dents_per_inch": 12, "ends_per_dent": 2},
            ],
        )

    def test_12_epi_skips_five_ends_in_a_dent(self):
        dents = [choice["dents_per_inch"] for choice in reed_choices(12)]
        self.assertEqual(dents, [6, 12])

    def test_odd_sett_has_no_common_reed(self):
        self.assertEqual(reed_choices(7), [])


if __name__ == "__main__":
    unittest.main()
