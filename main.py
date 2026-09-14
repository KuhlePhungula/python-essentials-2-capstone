# The Menu. Imports from every other module and puts everything together

from models import Student, HonoursStudent
from data_tools import generate_data_file, load_students, export_report, log_event
from analytics import passing_students, make_grader, class_average, highest, lowest, pass_rate, top_two_score
from reporting import enviro_report, data_report

students = []

def build_students(records):
    for index, (name, score) in enumerate(records, start=1):
        student_id = f"S{index}"
        if score >= 60:
            student = HonoursStudent(name, student_id, score, research_topic="Data Science")
        else:
            student = Student(name, student_id, score)
        students.append(student)
    return students

def get_int_input(prompt):
    raw = input(prompt)
    try:
        return int(raw)
    except ValueError:
        print(f"{raw} is not a valid number.")
        return None

def option_generate_data():
    path = generate_data_file()
    print(f"Sample data written to {path}")

def option_load_students():
    global students
    records = load_students()
    if not records:
        print("No records found. Generate the data file first (option 1).")
        return
    students = build_students(records)
    print(f"Loaded and cleaned {len(students)} students.")

def option_view_students():
    if not students:
        print("No students yet. Use option 2 first.")
        return
    for s in students:
        print(s)

def option_analyse():
    if not students:
        print("No students yet. Use option 2 first.")
        return

    top_student = max(students, key=lambda s: s.score)

    print(f"Class Average: {class_average(students):.1f}")
    print(f"Highest Score: {highest(students)}")
    print(f"Lowest score: {lowest(students)}")
    print(f"Pass Rate: {pass_rate(students):.1f}%")
    print(f"Top Student: {top_student}")
    print(f"Top two scores: {top_two_score(students)}")

def option_filter_generator():
    if not students:
        print("No students yet. Use option 2 first.")
        return
    print("Passing students:")
    for student in passing_students(students):
        print(student)

def option_custom_grader():
    if not students:
        print("No students yet. Use option 2 first.")
        return
    pass_mark = get_int_input("Enter a custom pass mark: ")
    if pass_mark is None:
        return

    grader = make_grader(pass_mark)
    stricter_grader = make_grader(pass_mark + 20)
    print(f"Grading with pass mark {pass_mark} and a stricter pass mark of {pass_mark + 20}")
    for s in students:
        print(f"  {s.name}: {s.score} -> {grader(s.score)} | stricter mark: {stricter_grader(s.score)}")


def option_report():
    enviro_report()
    print()
    data_report()

def option_export():
    if not students:
        print("No students yet. Use option 2 first.")
        return

    lines = ["Student Analytics Toolkit - Report", "=" * 35]
    for s in students:
        lines.append(str(s))
    lines.append("")
    lines.append(f"Class Average: {class_average(students):.1f}")
    lines.append(f"Pass Rate: {pass_rate(students):.1f}%")

    path = export_report("\n".join(lines))
    print(f"Report exported to {path}")


menu = """
===== STUDENT ANALYTICS TOOLKIT =====
1. Generate Sample Data File
2. Load and Clean Records from File
3. View All Students
4. Analyse (averages, pass/fail, top student)
5. Filter students (generator)
6. Grade with a custom pass mark (closure)
7. Environment and Date Report
8. Export results to a file
9. Exit"""

def main():
    log_event("Program started.")
    while True:
        print(menu)
        choice = input("Choose an option (1-9): ").strip()

        if choice == "1":
            option_generate_data()
        elif choice == "2":
            option_load_students()
        elif choice == "3":
            option_view_students()
        elif choice == "4":
            option_analyse()
        elif choice == "5":
            option_filter_generator()
        elif choice == "6":
            option_custom_grader()
        elif choice == "7":
            option_report()
        elif choice == "8":
            option_export()
        elif choice == "9":
            print("Goodbye!")
            log_event("Program exited")
            break
        else:
            print(f"{choice} is not a valid optiion. Please choose 1-9.")

if __name__ == "__main__":
    main()


