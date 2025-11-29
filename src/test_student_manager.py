import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.student_manager import StudentManager


class TestStudentManager(unittest.TestCase):
    def setUp(self):
        self.manager = StudentManager()

    def test_add_student(self):
        result = self.manager.add_student("2024001", "张三", "计算机1班")
        self.assertEqual(result, "学生 张三 添加成功")
        self.assertIn("2024001", self.manager.students)

    def test_add_duplicate_student(self):
        self.manager.add_student("2024001", "张三", "计算机1班")
        with self.assertRaises(ValueError):
            self.manager.add_student("2024001", "李四", "计算机2班")

    def test_add_grade(self):
        self.manager.add_student("2024001", "张三", "计算机1班")
        result = self.manager.add_grade("2024001", "数学", 85)
        self.assertEqual(result, "学生 张三 的 数学 成绩添加成功: 85")
        self.assertEqual(self.manager.students["2024001"]['grades']['数学'], 85)


if __name__ == '__main__':
    unittest.main()