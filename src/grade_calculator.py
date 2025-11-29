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

    def calculate_weighted_average(self, grades_dict, weights_dict):
        """计算加权平均分 - feature分支版本"""
        total = 0
        total_weight = 0
        for course, grade in grades_dict.items():
            weight = weights_dict.get(course, 1)
            total += grade * weight
            total_weight += weight
        return total / total_weight if total_weight > 0 else 0

    def calculate_semester_gpa(self, grades_dict, credit_dict):
        """计算学期GPA - develop分支版本"""
        total_points = 0
        total_credits = 0
        for course, grade in grades_dict.items():
            credit = credit_dict.get(course, 1)
            if grade >= 90:
                points = 4.0
            elif grade >= 80:
                points = 3.0
            elif grade >= 70:
                points = 2.0
            elif grade >= 60:
                points = 1.0
            else:
                points = 0.0
            total_points += points * credit
            total_credits += credit
        return total_points / total_credits if total_credits > 0 else 0


def generate_grade_report(self, students_data):
    """生成成绩报告"""
    report = []
    for student_id, info in students_data.items():
        grades = info['grades']
        if grades:
            total = sum(grades.values())
            count = len(grades)
            avg = total / count
            level = self.get_grade_level(avg)
            report.append({
                '学号': student_id,
                '姓名': info['name'],
                '平均分': round(avg, 2),
                '等级': level
            })
    return report


def calculate_grade_statistics(self, grades_data):
    """计算成绩统计数据"""
    statistics = {}
    for course, grades in grades_data.items():
        if grades:
            statistics[course] = {
                'average': sum(grades) / len(grades),
                'max': max(grades),
                'min': min(grades),
                'count': len(grades)
            }
    return statistics
