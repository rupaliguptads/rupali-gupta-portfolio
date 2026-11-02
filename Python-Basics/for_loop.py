# Python For Loop Examples

# Example 1: Print numbers from 1 to 10
print("Numbers from 1 to 10:")

for number in range(1, 11):
    print(number)


# Example 2: Print even numbers from 2 to 10

print("\nEven numbers:")

for number in range(2, 11, 2):
    print(number)


# Example 3: Multiplication table of 5

number = 5
print("\nMultiplication table of", number)

for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# Example 4: Sum of numbers from 1 to 10
total = 0

for number in range(1, 11):
    total += number

print("\nSum from 1 to 10:", total)
