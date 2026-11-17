# Pandas Series Basics

import pandas as pd

# Example 1: Create a Series
marks = pd.Series([85, 90, 95, 78, 88])

print("Student Marks:")
print(marks)
print()

# Example 2: Create a Series with custom index
student_marks = pd.Series(
    [85, 90, 95],
    index=["Aman", "Priya", "Rahul"]
)

print("Marks with Student Names:")
print(student_marks)
print()

# Example 3: Access values using index
print("Priya's marks:", student_marks["Priya"])
print("Rahul's marks:", student_marks["Rahul"])
print()

# Example 4: Basic statistics
print("Average Marks:", student_marks.mean())
print("Highest Marks:", student_marks.max())
print("Lowest Marks:", student_marks.min())
print()

# Example 5: Filter marks
print("Students scoring above 85:")
print(student_marks[student_marks > 85])
