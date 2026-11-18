# EDA Project - Step 5
# Handling Missing Values

import pandas as pd

data = {
    "Student": ["Aman", "Riya", "Rahul", "Neha", "Priya", "Karan"],
    "Age": [20, 21, None, 22, 20, 21],
    "Marks": [85, 92, 78, None, 95, 72],
    "City": ["Delhi", "Mumbai", "Delhi", "Jaipur", None, "Jaipur"]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Fill missing Age values with the median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Marks values with the mean
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Fill missing City values with the most frequent city
df["City"] = df["City"].fillna(df["City"].mode()[0])

print("\nCleaned Dataset:")
print(df)

# Verify that no missing values remain
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())
