"""Python basics assignment: conditionals, dictionaries, and file handling."""


def grade_for_score(score):
    """Return the letter grade for a score from 0 through 100."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def run_grade_checker():
    while True:
        try:
            score = int(input("Enter a score from 0 to 100: "))
            if 0 <= score <= 100:
                break
            print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Please enter a whole number.")
    print(f"Grade: {grade_for_score(score)}")


def manage_student_grades():
    students = {}

    while True:
        print("\nStudent Grades")
        print("1. Add a student")
        print("2. Update a student's grade")
        print("3. Print all student grades")
        print("4. Finish")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Student name: ").strip()
            grade = input("Student grade: ").strip()
            if name:
                students[name] = grade
                print("Student added.")
            else:
                print("Student name cannot be empty.")
        elif choice == "2":
            name = input("Student name to update: ").strip()
            if name in students:
                students[name] = input("New grade: ").strip()
                print("Grade updated.")
            else:
                print("Student not found.")
        elif choice == "3":
            if students:
                for name, grade in students.items():
                    print(f"{name}: {grade}")
            else:
                print("No student grades have been added yet.")
        elif choice == "4":
            return students
        else:
            print("Please choose 1, 2, 3, or 4.")


def write_and_read_file(students):
    filename = "student_grades.txt"

    # Write text to a file using open() and write().
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Student Grades\n")
        for name, grade in students.items():
            file.write(f"{name}: {grade}\n")

    # Read and display the file using open() and file.read().
    print(f"\nContents read from {filename}:")
    with open(filename, "r", encoding="utf-8") as file:
        contents = file.read()
        print(contents, end="")


def main():
    run_grade_checker()
    students = manage_student_grades()
    write_and_read_file(students)


if __name__ == "__main__":
    main()
