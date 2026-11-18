# Student Performance Analysis using Pandas

import pandas as pd

# Create a sample student dataset
data = {
    "Name": ["Aman", "Riya", "Rahul", "Priya", "Neha"],
    "Maths": [85, 92, 76, 95, 88],
    "Science": [90, 89, 80, 94, 91],
    "English": [78, 95, 82, 90, 87]
}

df = pd.DataFrame(data)

# Display the dataset
print("STUDENT DATASET")
print(df)

# Calculate total and average marks
subjects = ["Maths", "Science", "English"]
df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1)

print("\nSTUDENT PERFORMANCE")
print(df)

# Find the topper
topper = df.loc[df["Total"].idxmax()]

print("\nTOPPER")
print(topper["Name"])
print("Total Marks:", topper["Total"])

# Sort students by total marks
print("\nRANKING")
ranking = df.sort_values(by="Total", ascending=False)
print(ranking[["Name", "Total", "Average"]])

# Calculate subject-wise average
print("\nSUBJECT-WISE AVERAGE")
print(df[subjects].mean())

# Assign grades using apply and lambda
df["Grade"] = df["Average"].apply(
    lambda marks: "A" if marks >= 90
    else "B" if marks >= 80
    else "C"
)

print("\nFINAL RESULT")
print(df[["Name", "Total", "Average", "Grade"]])
