"""
成绩计算工具模块
"""


class GradeCalculator:
    @staticmethod
    def get_grade_level(score):
        """根据分数返回等级"""
        if score >= 90:
            return "优秀"
        elif score >= 80:
            return "良好"
        elif score >= 70:
            return "中等"
        elif score >= 60:
            return "及格"
        else:
            return "不及格"

    @staticmethod
    def calculate_class_average(students_data, course):
        """计算班级某课程平均分"""
        total = 0
        count = 0

        for student_id, student_info in students_data.items():
            if course in student_info['grades']:
                total += student_info['grades'][course]
                count += 1

        return total / count if count > 0 else 0

    @staticmethod
    def get_ranking(students_data):
        """按平均分排名"""
        student_scores = []

        for student_id, student_info in students_data.items():
            grades = student_info['grades'].values()
            if grades:
                avg_score = sum(grades) / len(grades)
                student_scores.append({
                    'student_id': student_id,
                    'name': student_info['name'],
                    'average': avg_score,
                    'grade_level': GradeCalculator.get_grade_level(avg_score)
                })

        # 按平均分降序排列
        return sorted(student_scores, key=lambda x: x['average'], reverse=True)