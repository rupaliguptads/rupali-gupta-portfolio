# Complete EDA Project
# Step 1: Dataset Creation and Initial Inspection

import pandas as pd

data = {
    "Student": ["Aman", "Riya", "Rahul", "Neha", "Priya",
                "Karan", "Simran", "Arjun", "Pooja", "Vikas"],
    "Age": [20, 21, 19, 22, 20, 21, 20, 23, 19, 22],
    "Study_Hours": [2, 4, 1, 5, 6, 3, 4, 2, 5, 3],
    "Marks": [55, 75, 45, 85, 95, 65, 90, 60, 88, 72],
    "City": ["Delhi", "Mumbai", "Delhi", "Jaipur", "Mumbai",
             "Jaipur", "Delhi", "Pune", "Mumbai", "Pune"]
}

df = pd.DataFrame(data)

print("===== DATASET OVERVIEW =====")

print("\nFirst Five Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())
