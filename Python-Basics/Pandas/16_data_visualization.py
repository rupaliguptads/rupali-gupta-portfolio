# Data Visualization using Pandas and Matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# Create sample student dataset
data = {
    "Name": ["Aman", "Riya", "Rahul", "Priya", "Neha"],
    "Marks": [85, 90, 75, 88, 92]
}

df = pd.DataFrame(data)

print("Student Dataset:")
print(df)

# Example 1: Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks - Bar Chart")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()

# Example 2: Line Chart
plt.figure(figsize=(8, 5))
plt.plot(df["Name"], df["Marks"], marker="o")
plt.title("Student Marks - Line Chart")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()

# Example 3: Histogram
plt.figure(figsize=(8, 5))
plt.hist(df["Marks"], bins=5, edgecolor="black")
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()
