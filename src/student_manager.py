"""
学生信息管理模块
"""


class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, class_name):
        """添加学生信息"""
        if student_id in self.students:
            raise ValueError(f"学生ID {student_id} 已存在")

        self.students[student_id] = {
            'name': name,
            'class': class_name,
            'grades': {}
        }
        return f"学生 {name} 添加成功"

    def add_grade(self, student_id, course, grade):
        """添加学生成绩"""
        if student_id not in self.students:
            raise ValueError(f"学生ID {student_id} 不存在")

        if not 0 <= grade <= 100:
            raise ValueError("成绩必须在0-100之间")

        self.students[student_id]['grades'][course] = grade
        return f"学生 {self.students[student_id]['name']} 的 {course} 成绩添加成功: {grade}"

    def get_student_info(self, student_id):
        """获取学生信息"""
        if student_id not in self.students:
            raise ValueError(f"学生ID {student_id} 不存在")

        return self.students[student_id]

    def get_all_students(self):
        """获取所有学生信息"""
        return self.students

    def calculate_average(self, student_id):
        """计算学生平均分"""
        student = self.get_student_info(student_id)
        grades = student['grades'].values()

        if not grades:
            return 0

        return sum(grades) / len(grades)

    def remove_student(self, student_id):
        """删除学生信息"""
        if student_id not in self.students:
            raise ValueError(f"学生ID {student_id} 不存在")

        student_name = self.students[student_id]['name']
        del self.students[student_id]
        return f"学生 {student_name} 删除成功"

    def get_student_count(self):
        """获取学生总数"""
        return len(self.students)

    def get_course_list(self):
        """获取所有课程列表"""
        courses = set()
        for student_info in self.students.values():
            courses.update(student_info['grades'].keys())
        return list(courses)