# EDA Project - Step 6
# Duplicate Record Analysis

import pandas as pd

data = {
    "Student": ["Aman", "Riya", "Rahul", "Neha", "Riya", "Karan"],
    "Age": [20, 21, 19, 22, 21, 20],
    "Marks": [85, 92, 78, 88, 92, 75],
    "City": ["Delhi", "Mumbai", "Delhi", "Jaipur", "Mumbai", "Pune"]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Count duplicate rows
print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())

# Display duplicate rows
print("\nDuplicate Records:")
print(df[df.duplicated()])

# Remove duplicate rows
df_cleaned = df.drop_duplicates()

print("\nDataset After Removing Duplicates:")
print(df_cleaned)

# Verify duplicates are removed
print("\nDuplicates Remaining:")
print(df_cleaned.duplicated().sum())
