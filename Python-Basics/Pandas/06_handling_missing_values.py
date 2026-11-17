# Handling Missing Values in Pandas

import pandas as pd

# Create a DataFrame with missing values
data = {
    "Name": ["Aman", "Riya", "Neha", "Rahul"],
    "Marks": [85, None, 92, None],
    "Age": [20, 21, None, 22]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# 1. Check missing values
print("\nMissing Values:")
print(df.isnull())

# 2. Count missing values in each column
print("\nMissing Values Count:")
print(df.isnull().sum())

# 3. Remove rows containing missing values
print("\nAfter dropna():")
print(df.dropna())

# 4. Fill missing marks with the average
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# 5. Fill missing ages with 0
df["Age"] = df["Age"].fillna(0)

print("\nAfter Filling Missing Values:")
print(df)

# 6. Check whether any missing values remain
print("\nFinal Missing Values Count:")
print(df.isnull().sum())
