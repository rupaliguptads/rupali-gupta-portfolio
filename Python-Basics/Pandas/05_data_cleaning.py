# Pandas Data Cleaning

import pandas as pd

# Create sample data with missing values and duplicates
data = {
    "Name": ["Aman", "Riya", "Aman", "Neha", None],
    "Marks": [85, 92, 85, None, 78],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(df)

# Fill missing names
df["Name"] = df["Name"].fillna("Unknown")

# Fill missing marks with the average
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nAfter Handling Missing Values:")
print(df)

# Check the cleaned data
print("\nFinal Data Information:")
print(df.info())
