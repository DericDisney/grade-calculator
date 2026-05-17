# Student Grade Calculator
# Author: Deric Disney
# Description: Calculates grades, GPA, and pass/fail status for multiple subjects

def get_grade(marks):
    """Return grade letter and grade point based on marks."""
    if marks >= 90:
        return 'A+', 10
    elif marks >= 80:
        return 'A', 9
    elif marks >= 70:
        return 'B+', 8
    elif marks >= 60:
        return 'B', 7
    elif marks >= 50:
        return 'C', 6
    elif marks >= 40:
        return 'D', 5
    else:
        return 'F', 0

def calculate_gpa(subjects):
    """Calculate GPA based on subject marks and credits."""
    total_credits = 0
    total_grade_points = 0

    for subject in subjects:
        grade_letter, grade_point = get_grade(subject['marks'])
        subject['grade'] = grade_letter
        subject['grade_point'] = grade_point
        total_grade_points += grade_point * subject['credits']
        total_credits += subject['credits']

    gpa = total_grade_points / total_credits if total_credits > 0 else 0
    return round(gpa, 2), total_credits

def display_result(subjects, gpa):
    """Display the result in a formatted table."""
    print("\n" + "=" * 65)
    print(f"{'STUDENT GRADE REPORT':^65}")
    print("=" * 65)
    print(f"{'Subject':<25} {'Marks':>6} {'Credits':>8} {'Grade':>7} {'GP':>5}")
    print("-" * 65)

    failed = []
    for s in subjects:
        print(f"{s['name']:<25} {s['marks']:>6} {s['credits']:>8} {s['grade']:>7} {s['grade_point']:>5}")
        if s['grade'] == 'F':
            failed.append(s['name'])

    print("-" * 65)
    print(f"\n{'GPA':>40}: {gpa}")

    if failed:
        print(f"\n⚠  Failed Subjects: {', '.join(failed)}")
        print("   Status: FAIL — Please re-appear in the following subjects.")
    else:
        print("\n✔  Status: PASS")

    print("=" * 65)

def main():
    print("=" * 65)
    print(f"{'STUDENT GRADE CALCULATOR':^65}")
    print("=" * 65)

    subjects = []

    try:
        n = int(input("\nEnter number of subjects: "))
        if n <= 0:
            print("Number of subjects must be positive.")
            return

        print()
        for i in range(n):
            print(f"--- Subject {i + 1} ---")
            name = input("  Subject name: ").strip()
            if not name:
                name = f"Subject {i + 1}"

            while True:
                try:
                    marks = float(input("  Marks obtained (0-100): "))
                    if 0 <= marks <= 100:
                        break
                    print("  Please enter marks between 0 and 100.")
                except ValueError:
                    print("  Invalid input. Please enter a number.")

            while True:
                try:
                    credits = int(input("  Credit hours: "))
                    if credits > 0:
                        break
                    print("  Credits must be a positive integer.")
                except ValueError:
                    print("  Invalid input. Please enter a whole number.")

            subjects.append({'name': name, 'marks': marks, 'credits': credits})
            print()

        gpa, total_credits = calculate_gpa(subjects)
        display_result(subjects, gpa)
        print(f"\n  Total Credits: {total_credits}")
        print()

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except KeyboardInterrupt:
        print("\n\nExited.")

if __name__ == "__main__":
    main()
