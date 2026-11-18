# EDA Project - Step 4
# Data Quality Check

import pandas as pd

data = {
    "Student": ["Aman", "Riya", "Rahul", "Neha", "Priya", "Karan"],
    "Age": [20, 21, None, 22, 20, 21],
    "Marks": [85, 92, 78, None, 95, 72],
    "City": ["Delhi", "Mumbai", "Delhi", "Jaipur", None, "Jaipur"]
}

df = pd.DataFrame(data)

# 1. Display the dataset
print("Original Dataset:")
print(df)

# 2. Count missing values in each column
print("\nMissing Values Per Column:")
print(df.isnull().sum())

# 3. Count all missing values
print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

# 4. Calculate missing value percentages
print("\nMissing Value Percentage:")
print((df.isnull().mean() * 100).round(2))

# 5. Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())
