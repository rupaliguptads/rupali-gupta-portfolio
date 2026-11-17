# Pandas Data Sorting

import pandas as pd

# Create a sample dataset
data = {
    "Name": ["Aman", "Riya", "Rahul", "Priya", "Neha"],
    "Marks": [85, 92, 78, 95, 88],
    "Age": [21, 22, 20, 23, 21],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Example 1: Sort by marks in ascending order
print("\nMarks: Lowest to Highest")
print(df.sort_values(by="Marks"))

# Example 2: Sort by marks in descending order
print("\nMarks: Highest to Lowest")
print(df.sort_values(by="Marks", ascending=False))

# Example 3: Sort by name alphabetically
print("\nNames: A to Z")
print(df.sort_values(by="Name"))

# Example 4: Sort by multiple columns
print("\nSort by City and then Marks")
print(df.sort_values(by=["City", "Marks"]))

# Example 5: Display the top 3 students by marks
print("\nTop 3 Students")
print(df.nlargest(3, "Marks"))
