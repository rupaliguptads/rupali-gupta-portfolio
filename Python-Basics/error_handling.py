# Python Error Handling Examples

# Example 1: Handle division by zero
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter a valid integer.")


# Example 2: Handle invalid number input
try:
    age = int(input("\nEnter your age: "))
    print("Your age is:", age)
except ValueError:
    print("Error: Age must be a whole number.")


# Example 3: Handle multiple exceptions
try:
    numbers = [10, 20, 30]
    index = int(input("\nEnter an index (0-2): "))
    print("Selected value:", numbers[index])
except ValueError:
    print("Error: Please enter an integer.")
except IndexError:
    print("Error: Index is out of range.")


# Example 4: Use finally
try:
    print("\nProcessing started.")
    result = 10 / 2
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Processing completed.")


# Example 5: Raise a custom error
def check_marks(marks):
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")
    return "Valid marks"


try:
    print(check_marks(85))
except ValueError as error:
    print("Error:", error)
