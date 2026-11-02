# Python Tuple Examples

# Example 1: Creating a tuple
fruits = ("apple", "banana", "mango")

print("Fruits:", fruits)
print("Type:", type(fruits))


# Example 2: Accessing tuple elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])


# Example 3: Tuple slicing
numbers = (10, 20, 30, 40, 50)

print("First three numbers:", numbers[:3])


# Example 4: Tuple length
print("Number of fruits:", len(fruits))


# Example 5: Checking whether an item exists
if "mango" in fruits:
    print("Mango is available")


# Example 6: Tuple unpacking
student = ("Rupali", 20, "CSE")

name, age, branch = student

print("Name:", name)
print("Age:", age)
print("Branch:", branch)


# Example 7: Single-element tuple
single_item = ("Python",)

print("Single-element tuple:", single_item)
print("Type:", type(single_item))
