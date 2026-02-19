import unittest

from heddle.yarns import lookup_yarn, yarn_names


class YarnTests(unittest.TestCase):
    def test_names_are_sorted(self):
        self.assertEqual(
            yarn_names(),
            ["10/2 cotton", "5/2 cotton", "8/2 cotton", "8/4 cotton"],
        )

    def test_lookup_ignores_case(self):
        yarn = lookup_yarn("  8/2 Cotton ")
        self.assertEqual(yarn["name"], "8/2 cotton")
        self.assertEqual(yarn["yards_per_pound"], 3360)

    def test_unknown_yarn(self):
        self.assertIsNone(lookup_yarn("silk"))
        self.assertIsNone(lookup_yarn(None))


if __name__ == "__main__":
    unittest.main()
