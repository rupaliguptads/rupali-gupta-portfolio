# Python Dictionary Comprehensions

# Example 1: Create a dictionary of squares
squares = {number: number ** 2 for number in range(1, 6)}
print("Squares:", squares)


# Example 2: Create a dictionary of even numbers and their squares
even_squares = {
    number: number ** 2
    for number in range(1, 11)
    if number % 2 == 0
}
print("Even number squares:", even_squares)


# Example 3: Convert names to uppercase
names = ["Rupali", "Aman", "Neha"]

uppercase_names = {
    name: name.upper()
    for name in names
}
print("Uppercase names:", uppercase_names)


# Example 4: Create a dictionary from two lists
students = ["Aman", "Rupali", "Neha"]
marks = [75, 90, 82]

student_marks = {
    students[index]: marks[index]
    for index in range(len(students))
}
print("Student marks:", student_marks)


# Example 5: Filter students who scored 80 or more
top_students = {
    name: mark
    for name, mark in student_marks.items()
    if mark >= 80
}
print("Students scoring 80 or more:", top_students)
