# EDA Project - Step 3
# Dataset Summary and Basic Statistics

import pandas as pd

data = {
    "Student": ["Aman", "Riya", "Rahul", "Neha", "Priya", "Karan"],
    "Age": [20, 21, 19, 22, 20, 21],
    "Marks": [85, 92, 78, 88, 95, 72],
    "City": ["Delhi", "Mumbai", "Delhi", "Jaipur", "Mumbai", "Jaipur"]
}

df = pd.DataFrame(data)

# 1. Summary of numerical columns
print("Statistical Summary:")
print(df.describe())

# 2. Average marks
print("\nAverage Marks:")
print(df["Marks"].mean())

# 3. Highest marks
print("\nHighest Marks:")
print(df["Marks"].max())

# 4. Lowest marks
print("\nLowest Marks:")
print(df["Marks"].min())

# 5. Unique cities
print("\nUnique Cities:")
print(df["City"].unique())

# 6. Number of students in each city
print("\nStudents in Each City:")
print(df["City"].value_counts())
