# Reading and Writing CSV Files using Pandas

import pandas as pd

# Create a sample dataset
data = {
    "Name": ["Aman", "Riya", "Rahul", "Priya", "Neha"],
    "Age": [21, 22, 20, 23, 21],
    "Marks": [85, 92, 76, 88, 95]
}

df = pd.DataFrame(data)

# Display the original dataset
print("Original Dataset:")
print(df)

# Save the dataset to a CSV file
df.to_csv("students.csv", index=False)
print("\nDataset saved to students.csv")

# Read the CSV file
loaded_df = pd.read_csv("students.csv")

print("\nDataset Read from CSV:")
print(loaded_df)

# Display basic information
print("\nDataset Shape:")
print(loaded_df.shape)

print("\nColumn Names:")
print(loaded_df.columns.tolist())

print("\nAverage Marks:")
print(loaded_df["Marks"].mean())
