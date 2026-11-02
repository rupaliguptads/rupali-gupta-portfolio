# Python Sets Examples

# Example 1: Create a set
fruits = {"apple", "banana", "mango"}

print("Fruits:", fruits)


# Example 2: Sets automatically remove duplicates
numbers = {10, 20, 10, 30, 20, 40}

print("Unique numbers:", numbers)


# Example 3: Add and remove elements
fruits.add("orange")
print("After adding orange:", fruits)

fruits.remove("banana")
print("After removing banana:", fruits)


# Example 4: Check whether an item exists
if "mango" in fruits:
    print("Mango is available")


# Example 5: Union of sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Union:", set_a | set_b)


# Example 6: Intersection of sets
print("Intersection:", set_a & set_b)


# Example 7: Difference of sets
print("Difference:", set_a - set_b)


# Example 8: Symmetric difference
print("Symmetric difference:", set_a ^ set_b)
