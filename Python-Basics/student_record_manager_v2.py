# Student Record Manager - Version 2
# Stores student records permanently using JSON

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("students.json")


def load_students():
    """Load student records from the JSON file."""
    if not DATA_FILE.exists():
        return {}

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, dict):
            return data

        print("Invalid data format. Starting with empty records.")
        return {}

    except (json.JSONDecodeError, OSError) as error:
        print(f"Could not load records: {error}")
        return {}


def save_students(students):
    """Save student records to the JSON file."""
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)

        return True

    except OSError as error:
        print(f"Could not save records: {error}")
        return False


def add_student(students):
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

    if save_students(students):
        print("Student added and saved successfully!")
    else:
        del students[student_id]
        print("Student was not saved. Please try again.")


def display_students(students):
    if not students:
        print("No student records available.")
        return

    print("\n--- Student Records ---")

    for student_id, details in students.items():
        print(f"ID: {student_id}")
        print(f"Name: {details['name']}")
        print(f"Marks: {details['marks']}")
        print("-" * 25)


def search_student(students):
    student_id = input("Enter student ID to search: ").strip()

    if student_id in students:
        details = students[student_id]
        print(f"Name: {details['name']}")
        print(f"Marks: {details['marks']}")
    else:
        print("Student not found.")


def calculate_average(students):
    if not students:
        print("No records available.")
        return

    total = sum(
        details["marks"] for details in students.values()
    )
    average = total / len(students)

    print(f"Average marks: {average:.2f}")


def main():
    students = load_students()
    print(f"Loaded {len(students)} saved student record(s).")

    while True:
        print("\n===== Student Record Manager V2 =====")
        print("1. Add student")
        print("2. Display all students")
        print("3. Search student")
        print("4. Calculate average marks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            calculate_average(students)
        elif choice == "5":
            print("Thank you for using Student Record Manager V2!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()
