# Data Filtering in Pandas

import pandas as pd

# Create a sample DataFrame
data = {
    "Name": ["Aman", "Priya", "Rahul", "Neha", "Ravi"],
    "Marks": [85, 90, 95, 78, 65],
    "City": ["Delhi", "Lucknow", "Jaipur", "Agra", "Delhi"]
}

df = pd.DataFrame(data)

print("Complete DataFrame:")
print(df)

# Example 1: Filter students scoring 85 or more
print("\nStudents scoring 85 or more:")
print(df[df["Marks"] >= 85])

# Example 2: Filter students scoring below 80
print("\nStudents scoring below 80:")
print(df[df["Marks"] < 80])

# Example 3: Filter students from Delhi
print("\nStudents from Delhi:")
print(df[df["City"] == "Delhi"])

# Example 4: Use two conditions
print("\nStudents scoring 80 or more and from Delhi:")
print(df[(df["Marks"] >= 80) & (df["City"] == "Delhi")])

# Example 5: Sort students by marks
print("\nStudents sorted by marks, highest first:")
print(df.sort_values(by="Marks", ascending=False))
