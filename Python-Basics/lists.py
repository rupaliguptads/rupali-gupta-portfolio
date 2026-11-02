# Python Lists Examples

# Example 1: Create and print a list
fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Fruits:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])


# Example 2: Add and remove items
fruits.append("Grapes")
print("After adding:", fruits)

fruits.remove("Banana")
print("After removing:", fruits)


# Example 3: Update a list item
numbers = [10, 20, 30, 40]
numbers[1] = 25

print("Updated numbers:", numbers)


# Example 4: Loop through a list
print("List items:")

for fruit in fruits:
    print(fruit)


# Example 5: Find sum, minimum and maximum
numbers = [15, 5, 25, 10, 20]

print("Sum:", sum(numbers))
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))


# Example 6: Sort a list
numbers.sort()
print("Ascending order:", numbers)

numbers.sort(reverse=True)
print("Descending order:", numbers)


# Example 7: List comprehension
squares = [number ** 2 for number in range(1, 6)]

print("Squares:", squares)
