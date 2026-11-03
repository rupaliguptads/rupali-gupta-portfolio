# Python mini-project
# Student Record Manager

students = {}

def add_student():
    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if student_id in students:
        print("This student ID already exists.")
        return

    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    try:
        marks = float(input("Enter marks (0-100): "))

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter valid numeric marks.")
        return

    students[student_id] = {
        "name": name,
        "marks": marks
    }

    print("Student added successfully!")


def display_students():
    if not students:
        print("No student records available.")
        return

    print("\n--- Student Records ---")

    for student_id, details in students.items():
        print(f"ID: {student_id}")
        print(f"Name: {details['name']}")
        print(f"Marks: {details['marks']}")
        print("-" * 25)


def search_student():
    student_id = input("Enter student ID to search: ").strip()

    if student_id in students:
        details = students[student_id]
        print("Student found!")
        print(f"Name: {details['name']}")
        print(f"Marks: {details['marks']}")
    else:
        print("Student not found.")


def calculate_average():
    if not students:
        print("No records available to calculate average.")
        return

    total_marks = sum(
        details["marks"] for details in students.values()
    )

    average = total_marks / len(students)
    print(f"Average marks: {average:.2f}")


def main():
    while True:
        print("\n===== Student Record Manager =====")
        print("1. Add student")
        print("2. Display all students")
        print("3. Search student")
        print("4. Calculate average marks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            calculate_average()
        elif choice == "5":
            print("Thank you for using Student Record Manager!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()
