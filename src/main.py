"""
主程序 - 学生成绩管理系统
"""
from student_manager import StudentManager
from grade_calculator import GradeCalculator


def main():
    manager = StudentManager()

    while True:
        print("\n=== 学生成绩管理系统 ===")
        print("1. 添加学生")
        print("2. 添加成绩")
        print("3. 查询学生信息")
        print("4. 查看所有学生")
        print("5. 计算平均分")
        print("6. 成绩排名")
        print("7. 退出")

        choice = input("请选择操作 (1-7): ")

        try:
            if choice == '1':
                student_id = input("输入学号: ")
                name = input("输入姓名: ")
                class_name = input("输入班级: ")
                result = manager.add_student(student_id, name, class_name)
                print(result)

            elif choice == '2':
                student_id = input("输入学号: ")
                course = input("输入课程名: ")
                grade = float(input("输入成绩: "))
                result = manager.add_grade(student_id, course, grade)
                print(result)

            elif choice == '3':
                student_id = input("输入学号: ")
                info = manager.get_student_info(student_id)
                print(f"学生信息: {info}")

            elif choice == '4':
                students = manager.get_all_students()
                for sid, info in students.items():
                    print(f"学号: {sid}, 姓名: {info['name']}, 班级: {info['class']}")

            elif choice == '5':
                student_id = input("输入学号: ")
                avg = manager.calculate_average(student_id)
                level = GradeCalculator.get_grade_level(avg)
                print(f"平均分: {avg:.2f}, 等级: {level}")

            elif choice == '6':
                ranking = GradeCalculator.get_ranking(manager.get_all_students())
                print("=== 成绩排名 ===")
                for i, student in enumerate(ranking, 1):
                    print(f"{i}. {student['name']} - 平均分: {student['average']:.2f} ({student['grade_level']})")

            elif choice == '7':
                print("感谢使用学生成绩管理系统！")
                break

            else:
                print("无效选择，请重新输入！")

        except Exception as e:
            print(f"操作失败: {e}")


if __name__ == "__main__":
    main()