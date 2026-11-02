# Python Lambda, Map, and Filter

# Example 1: Lambda function
square = lambda number: number ** 2
print("Square of 5:", square(5))


# Example 2: Lambda with two arguments
add = lambda a, b: a + b
print("Sum:", add(10, 20))


# Example 3: Using map() to square numbers
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda number: number ** 2, numbers))
print("Squares:", squares)


# Example 4: Using map() to convert temperatures
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(
    map(lambda temperature: (temperature * 9 / 5) + 32, celsius)
)
print("Fahrenheit:", fahrenheit)


# Example 5: Using filter() to get even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print("Even numbers:", even_numbers)


# Example 6: Using filter() to get passing marks
marks = [25, 45, 67, 32, 89, 38, 76]
passing_marks = list(filter(lambda mark: mark >= 40, marks))
print("Passing marks:", passing_marks)


# Example 7: Sorting students by marks
students = [("Aman", 75), ("Rupali", 90), ("Neha", 82)]
sorted_students = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)
print("Students sorted by marks:", sorted_students)


# Example 8: Using map() and filter() together
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = list(
    map(
        lambda number: number ** 2,
        filter(lambda number: number % 2 == 0, numbers)
    )
)
print("Squares of even numbers:", even_squares)
