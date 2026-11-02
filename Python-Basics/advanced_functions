# Advanced Python Functions

# Example 1: Default arguments
def greet(name, message="Welcome to Python!"):
    print(f"Hello, {name}. {message}")


greet("Rupali")
greet("Rupali", "Keep learning every day!")


# Example 2: Keyword arguments
def student_info(name, course):
    print(f"Name: {name}")
    print(f"Course: {course}")


student_info(course="BTech CSE", name="Rupali")


# Example 3: Variable-length arguments (*args)
def calculate_sum(*args):
    return sum(args)


print("Sum:", calculate_sum(10, 20, 30))
print("Sum:", calculate_sum(5, 10, 15, 20))


# Example 4: Keyword variable arguments (**kwargs)
def display_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


display_details(name="Rupali", skill="Python", level="Beginner")


# Example 5: Lambda function
square = lambda number: number ** 2

print("Square of 5:", square(5))


# Example 6: Using lambda with sorted()
students = [("Aman", 75), ("Rupali", 90), ("Neha", 82)]

students_sorted = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print("Students by marks:", students_sorted)


# Example 7: Recursive function
def factorial(number):
    if number < 0:
        raise ValueError("Number must be non-negative.")

    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)


print("Factorial of 5:", factorial(5))
