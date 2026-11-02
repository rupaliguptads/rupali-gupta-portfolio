# Python While Loop Examples

# Example 1: Print numbers from 1 to 10

print("Numbers from 1 to 10:")

number = 1
while number <= 10:
    print(number)
    number += 1


# Example 2: Print even numbers from 2 to 10
print("\nEven numbers:")

number = 2
while number <= 10:
    print(number)
    number += 2

# Example 3: Multiplication table of 5
print("\nMultiplication table of 5:")

number = 1
while number <= 10:
    print(5, "x", number, "=", 5 * number)
    number += 1

# Example 4: Calculate the sum from 1 to 10
total = 0
number = 1

while number <= 10:
    total += number
    number += 1

print("\nSum from 1 to 10:", total)
