# Python Dictionaries Examples

# Example 1: Create and print a dictionary
student = {
    "name": "Rupali",
    "age": 20,
    "course": "BTech CSE",
    "marks": 85
}

print("Student details:", student)
print("Name:", student["name"])
print("Marks:", student["marks"])


# Example 2: Add a new key-value pair
student["city"] = "Delhi"
print("After adding city:", student)


# Example 3: Update a value
student["marks"] = 90
print("Updated marks:", student["marks"])


# Example 4: Remove a key-value pair
student.pop("age")
print("After removing age:", student)


# Example 5: Loop through dictionary items
print("\nStudent information:")

for key, value in student.items():
    print(key, ":", value)


# Example 6: Check whether a key exists
if "name" in student:
    print("\nName is available in the dictionary.")


# Example 7: Dictionary methods
print("\nKeys:", student.keys())
print("Values:", student.values())


# Example 8: Count frequency of items
fruits = ["apple", "banana", "apple", "mango", "banana", "apple"]
frequency = {}

for fruit in fruits:
    frequency[fruit] = frequency.get(fruit, 0) + 1

print("\nFruit frequency:", frequency)
