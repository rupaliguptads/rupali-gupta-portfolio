# Selecting Rows and Columns in Pandas

import pandas as pd

# Create a sample DataFrame
data = {
    "Name": ["Aman", "Priya", "Rahul", "Neha"],
    "Marks": [85, 90, 95, 78],
    "City": ["Delhi", "Lucknow", "Jaipur", "Agra"]
}

df = pd.DataFrame(data)

print("Complete DataFrame:")
print(df)

# Example 1: Select a single column
print("\nStudent Names:")
print(df["Name"])

# Example 2: Select multiple columns
print("\nNames and Marks:")
print(df[["Name", "Marks"]])

# Example 3: Select a row using loc
print("\nFirst student using loc:")
print(df.loc[0])

# Example 4: Select rows using iloc
print("\nFirst two rows using iloc:")
print(df.iloc[0:2])

# Example 5: Select a specific value
print("\nPriya's marks:")
print(df.loc[1, "Marks"])

# Example 6: Select rows based on a condition
print("\nStudents scoring 85 or more:")
print(df[df["Marks"] >= 85])
