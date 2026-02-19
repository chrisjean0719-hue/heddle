import unittest

from heddle.validate import validate_project


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


class ValidateTests(unittest.TestCase):
    def test_sample_is_valid(self):
        self.assertEqual(validate_project(project()), [])

    def test_rejects_a_list(self):
        self.assertEqual(validate_project([]), ["project: Project must be an object"])

    def test_reports_each_bad_field(self):
        errors = validate_project(
            project(name="  ", yarn="silk", widthIn=0, epi=1.5, lengthIn=-1, loomWasteIn=-2, shafts=1)
        )
        self.assertIn("name: Project needs a name", errors)
        self.assertTrue(any(item.startswith("yarn:") for item in errors))
        self.assertIn("widthIn: widthIn must be a positive number of inches", errors)
        self.assertIn("epi: epi must be a positive integer", errors)
        self.assertIn("lengthIn: lengthIn must be a positive number of inches", errors)
        self.assertIn("loomWasteIn: loomWasteIn must be zero or more inches", errors)
        self.assertIn("shafts: shafts must be an integer from 2 to 16", errors)

    def test_allows_zero_waste(self):
        self.assertEqual(validate_project(project(loomWasteIn=0)), [])


if __name__ == "__main__":
    unittest.main()
