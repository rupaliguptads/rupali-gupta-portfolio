# EDA Project - Step 9
# Grouped Data Analysis

import pandas as pd

data = {
    "Student": ["Aman", "Riya", "Rahul", "Neha", "Priya", "Karan", "Simran"],
    "City": ["Delhi", "Mumbai", "Delhi", "Jaipur", "Mumbai", "Jaipur", "Delhi"],
    "Marks": [85, 92, 78, 88, 95, 72, 90]
}

df = pd.DataFrame(data)

print("Student Dataset:")
print(df)

# Calculate average marks for each city
print("\nAverage Marks by City:")
print(df.groupby("City")["Marks"].mean().round(2))

# Count students in each city
print("\nNumber of Students by City:")
print(df.groupby("City")["Student"].count())

# Calculate multiple statistics
print("\nCity-wise Summary:")
summary = df.groupby("City")["Marks"].agg(
    ["count", "mean", "min", "max"]
)

print(summary.round(2))

# Identify the city with the highest average marks
average_marks = df.groupby("City")["Marks"].mean()
top_city = average_marks.idxmax()

print("\nCity with Highest Average Marks:", top_city)
print("Average Marks:", round(average_marks.max(), 2))
