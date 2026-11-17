# Pandas GroupBy and Aggregation

import pandas as pd

# Create a sample student dataset
data = {
    "Name": ["Aman", "Riya", "Rahul", "Priya", "Neha", "Arjun"],
    "Subject": ["Math", "Science", "Math", "Science", "Math", "Science"],
    "Marks": [85, 90, 78, 95, 88, 82],
    "City": ["Delhi", "Mumbai", "Delhi", "Mumbai", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data)

print("Complete Dataset:")
print(df)

# Example 1: Average marks by subject
print("\nAverage Marks by Subject:")
print(df.groupby("Subject")["Marks"].mean())

# Example 2: Total marks by subject
print("\nTotal Marks by Subject:")
print(df.groupby("Subject")["Marks"].sum())

# Example 3: Number of students in each city
print("\nStudents by City:")
print(df.groupby("City")["Name"].count())

# Example 4: Multiple statistics by subject
print("\nSubject-wise Statistics:")
print(df.groupby("Subject")["Marks"].agg(["count", "mean", "max", "min"]))

# Example 5: Sort groups by average marks
print("\nSubjects Sorted by Average Marks:")
print(df.groupby("Subject")["Marks"].mean().sort_values(ascending=False))
