# Statistical Analysis using Pandas

import pandas as pd

# Create a sample dataset
data = {
    "Student": ["Aman", "Riya", "Rahul", "Neha", "Priya"],
    "Maths": [85, 92, 78, 88, 95],
    "Science": [80, 89, 75, 91, 94],
    "English": [82, 90, 80, 85, 93]
}

df = pd.DataFrame(data)

# Display the dataset
print("Student Dataset:")
print(df)

# Calculate descriptive statistics
print("\nDescriptive Statistics:")
print(df[["Maths", "Science", "English"]].describe())

# Calculate correlation between subjects
print("\nCorrelation Between Subjects:")
print(df[["Maths", "Science", "English"]].corr())

# Calculate total marks
df["Total"] = df[["Maths", "Science", "English"]].sum(axis=1)

# Calculate average marks
df["Average"] = df[["Maths", "Science", "English"]].mean(axis=1)

print("\nStudent Performance:")
print(df)

# Find the student with the highest total marks
top_student = df.loc[df["Total"].idxmax()]

print("\nTop Performing Student:")
print(top_student)
