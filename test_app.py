import unittest
from app import calculate_grade


class TestGradeCalculator(unittest.TestCase):

    def test_grade_a(self):
        self.assertEqual(calculate_grade([95, 90, 92]), "A")

    def test_grade_b(self):
        self.assertEqual(calculate_grade([80, 75, 78]), "B")


if __name__ == "__main__":
    unittest.main()