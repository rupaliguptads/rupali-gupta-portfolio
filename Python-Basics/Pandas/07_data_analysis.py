# Pandas Data Analysis and Summary Statistics

import pandas as pd

# Create a sample student dataset
data = {
    "Name": ["Aman", "Riya", "Neha", "Rahul", "Priya"],
    "Maths": [85, 92, 78, 88, 95],
    "Science": [90, 89, 82, 76, 91],
    "English": [80, 95, 85, 90, 88]
}

df = pd.DataFrame(data)

print("Student Dataset:")
print(df)

# 1. Display basic information
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

# 2. Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# 3. Calculate total marks
subjects = ["Maths", "Science", "English"]
df["Total"] = df[subjects].sum(axis=1)

# 4. Calculate average marks
df["Average"] = df[subjects].mean(axis=1)

# 5. Find the highest-scoring student
top_student = df.loc[df["Total"].idxmax()]

print("\nStudent Results:")
print(df)

print("\nHighest-Scoring Student:")
print(top_student["Name"])
print("Total Marks:", top_student["Total"])

# 6. Calculate subject-wise average
print("\nSubject-wise Average:")
print(df[subjects].mean())

# 7. Sort students by total marks
print("\nStudents Ranked by Total Marks:")
print(df.sort_values(by="Total", ascending=False))
