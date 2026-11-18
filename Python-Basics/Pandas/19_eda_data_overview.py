# Exploratory Data Analysis (EDA)
# Step 1: Understanding the Dataset

import pandas as pd

# Create a sample student dataset
data = {
    "Student": ["Aman", "Riya", "Rahul", "Neha", "Priya", "Karan"],
    "Maths": [85, 92, 78, 88, 95, 87],
    "Science": [80, 89, 75, 91, 94, 72],
    "English": [82, 90, 80, 85, 93, 76]
}

df = pd.DataFrame(data)

# 1. Display the dataset
print("===== STUDENT DATASET =====")
print(df)

# 2. Display the first five rows
print("\n===== FIRST FIVE ROWS =====")
print(df.head())

# 3. Check the number of rows and columns
print("\n===== DATASET SHAPE =====")
print(df.shape)

# 4. Check column names
print("\n===== COLUMN NAMES =====")
print(df.columns)

# 5. Check data types and non-null values
print("\n===== DATASET INFORMATION =====")
df.info()

# 6. Generate statistical summary
print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())
