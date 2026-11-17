# Pandas: merge(), join(), and concat()

import pandas as pd

# Dataset 1: Student details
students = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104],
    "Name": ["Aman", "Riya", "Rahul", "Priya"],
    "City": ["Delhi", "Mumbai", "Pune", "Delhi"]
})

# Dataset 2: Student marks
marks = pd.DataFrame({
    "Student_ID": [101, 102, 103, 105],
    "Marks": [85, 92, 78, 88]
})

print("Student Details:")
print(students)

print("\nStudent Marks:")
print(marks)

# Example 1: Inner merge
print("\nInner Merge:")
print(pd.merge(students, marks, on="Student_ID", how="inner"))

# Example 2: Left merge
print("\nLeft Merge:")
print(pd.merge(students, marks, on="Student_ID", how="left"))

# Example 3: Outer merge
print("\nOuter Merge:")
print(pd.merge(students, marks, on="Student_ID", how="outer"))

# Example 4: Concatenate datasets vertically
extra_students = pd.DataFrame({
    "Student_ID": [106],
    "Name": ["Neha"],
    "City": ["Jaipur"]
})

print("\nVertical Concatenation:")
print(pd.concat([students, extra_students], ignore_index=True))

# Example 5: Join using the index
student_names = students.set_index("Student_ID")[["Name"]]
student_cities = students.set_index("Student_ID")[["City"]]

print("\nJoin by Index:")
print(student_names.join(student_cities))
