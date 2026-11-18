# Pandas Pivot Table Examples

import pandas as pd

# Create a sample student dataset
data = {
    "Name": ["Aman", "Riya", "Rahul", "Priya", "Neha", "Arjun"],
    "Class": ["A", "A", "B", "B", "A", "B"],
    "Subject": ["Math", "Science", "Math", "Science", "Math", "Science"],
    "Marks": [85, 90, 75, 88, 92, 80]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Example 1: Average marks by class
class_average = pd.pivot_table(
    df,
    values="Marks",
    index="Class",
    aggfunc="mean"
)

print("\nAverage Marks by Class:")
print(class_average)

# Example 2: Average marks by class and subject
class_subject_average = pd.pivot_table(
    df,
    values="Marks",
    index="Class",
    columns="Subject",
    aggfunc="mean"
)

print("\nAverage Marks by Class and Subject:")
print(class_subject_average)

# Example 3: Total marks by class
class_total = pd.pivot_table(
    df,
    values="Marks",
    index="Class",
    aggfunc="sum"
)

print("\nTotal Marks by Class:")
print(class_total)

# Example 4: Number of students in each class
student_count = pd.pivot_table(
    df,
    values="Name",
    index="Class",
    aggfunc="count"
)

print("\nStudent Count by Class:")
print(student_count)
