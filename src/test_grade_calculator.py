import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.grade_calculator import GradeCalculator

class TestGradeCalculator(unittest.TestCase):
    def test_get_grade_level(self):
        self.assertEqual(GradeCalculator.get_grade_level(95), "优秀")
        self.assertEqual(GradeCalculator.get_grade_level(85), "良好")
        self.assertEqual(GradeCalculator.get_grade_level(75), "中等")
        self.assertEqual(GradeCalculator.get_grade_level(65), "及格")
        self.assertEqual(GradeCalculator.get_grade_level(55), "不及格")

if __name__ == '__main__':
    unittest.main()