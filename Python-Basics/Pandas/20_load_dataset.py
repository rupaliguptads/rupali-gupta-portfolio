# EDA Project - Step 2
# Load and Explore Dataset

import pandas as pd

# Create a sample dataset
data = {
    "Student": ["Aman", "Riya", "Rahul", "Neha", "Priya", "Karan"],
    "Age": [20, 21, 19, 22, 20, 21],
    "Marks": [85, 92, 78, 88, 95, 72],
    "City": ["Delhi", "Mumbai", "Delhi", "Jaipur", "Mumbai", "Jaipur"]
}

df = pd.DataFrame(data)

# Display the first five rows
print("First Five Rows:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display number of rows and columns
print("\nDataset Shape:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns.tolist())
