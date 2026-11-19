# EDA Project - Step 10
# Data Visualization using Matplotlib

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Student": ["Aman", "Riya", "Rahul", "Neha", "Priya", "Karan", "Simran"],
    "City": ["Delhi", "Mumbai", "Delhi", "Jaipur", "Mumbai", "Jaipur", "Delhi"],
    "Study_Hours": [2, 4, 1, 5, 6, 3, 4],
    "Marks": [55, 75, 45, 85, 95, 65, 90]
}

df = pd.DataFrame(data)

# Create three plots
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# 1. Histogram: distribution of marks
axes[0].hist(df["Marks"], bins=5, edgecolor="black")
axes[0].set_title("Distribution of Marks")
axes[0].set_xlabel("Marks")
axes[0].set_ylabel("Number of Students")

# 2. Bar chart: average marks by city
city_avg = df.groupby("City")["Marks"].mean()
axes[1].bar(city_avg.index, city_avg.values)
axes[1].set_title("Average Marks by City")
axes[1].set_xlabel("City")
axes[1].set_ylabel("Average Marks")
axes[1].tick_params(axis="x", rotation=30)

# 3. Scatter plot: study hours vs marks
axes[2].scatter(df["Study_Hours"], df["Marks"])
axes[2].set_title("Study Hours vs Marks")
axes[2].set_xlabel("Study Hours")
axes[2].set_ylabel("Marks")

plt.tight_layout()
plt.show()
