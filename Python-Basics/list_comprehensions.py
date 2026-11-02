# Python List Comprehensions

# Example 1: Create a list of squares
squares = [number ** 2 for number in range(1, 11)]
print("Squares:", squares)


# Example 2: Get even numbers
even_numbers = [number for number in range(1, 21) if number % 2 == 0]
print("Even numbers:", even_numbers)


# Example 3: Get odd numbers
odd_numbers = [number for number in range(1, 21) if number % 2 != 0]
print("Odd numbers:", odd_numbers)


# Example 4: Convert words to uppercase
words = ["python", "machine learning", "data science"]
uppercase_words = [word.upper() for word in words]
print("Uppercase words:", uppercase_words)


# Example 5: Filter words by length
names = ["Aman", "Rupali", "Neha", "Priya"]
long_names = [name for name in names if len(name) > 4]
print("Names longer than 4 characters:", long_names)


# Example 6: Extract positive numbers
numbers = [-5, 10, -2, 8, 0, 15]
positive_numbers = [number for number in numbers if number > 0]
print("Positive numbers:", positive_numbers)


# Example 7: Convert Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temperature * 9 / 5) + 32 for temperature in celsius]
print("Fahrenheit temperatures:", fahrenheit)
