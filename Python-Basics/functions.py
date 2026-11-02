# Python Functions Examples

# Example 1: Simple function
def greet():
    print("Hello, Rupali!")
    print("Welcome to Python programming.")

greet()

# Example 2: Function with parameters
def greet_user(name):
    print("Hello,", name)

greet_user("Rupali")
greet_user("Student")

# Example 3: Function that returns a value
def add(a, b):
    return a + b

result = add(10, 20)
print("Sum:", result)

# Example 4: Calculate the square of a number
def square(number):
    return number * number

print("Square of 5:", square(5))

# Example 5: Check whether a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("10 is", check_even_odd(10))
print("7 is", check_even_odd(7))

# Example 6: Calculate factorial
def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result *= i

    return result

print("Factorial of 5:", factorial(5))
