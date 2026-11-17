# Pandas DataFrame Basics

import pandas as pd

# Example 1: Create a DataFrame using a dictionary
data = {
    "Name": ["Aman", "Priya", "Rahul", "Neha"],
    "Marks": [85, 90, 95, 78],
    "City": ["Delhi", "Lucknow", "Jaipur", "Agra"]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)
print()

# Example 2: Display the first two rows
print("First two students:")
print(df.head(2))
print()

# Example 3: Display column names
print("Column names:")
print(df.columns.tolist())
print()

# Example 4: Display DataFrame information
print("Shape (rows, columns):", df.shape)
print("Number of rows:", len(df))
print()

# Example 5: Select a single column
print("Student marks:")
print(df["Marks"])
print()

# Example 6: Select multiple columns
print("Names and marks:")
print(df[["Name", "Marks"]])
