# Student Performance Analysis Project

import pandas as pd
import matplotlib.pyplot as plt

# 1. Create a sample dataset
data = {
    "Student": ["Aman", "Riya", "Rahul", "Neha", "Priya", "Karan"],
    "Maths": [85, 92, 78, 88, 95, None],
    "Science": [80, 89, 75, 91, 94, 72],
    "English": [82, 90, 80, 85, 93, 76]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# 2. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 3. Clean the dataset
df["Maths"] = df["Maths"].fillna(df["Maths"].mean())

# 4. Calculate total and average marks
subjects = ["Maths", "Science", "English"]

df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1)

# 5. Display analysis
print("\nCleaned Dataset:")
print(df.round(2))

print("\nClass Average:")
print(df[subjects].mean().round(2))

top_student = df.loc[df["Total"].idxmax()]
print("\nTop Performing Student:")
print(top_student)

# 6. Visualize average marks
plt.figure(figsize=(8, 5))
plt.bar(df["Student"], df["Average"])
plt.title("Student Average Marks")
plt.xlabel("Student")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.tight_layout()
plt.show()
