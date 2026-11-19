# EDA Project - Step 8
# Correlation Analysis

import pandas as pd

data = {
    "Student": ["Aman", "Riya", "Rahul", "Neha", "Priya", "Karan"],
    "Study_Hours": [2, 4, 1, 5, 6, 3],
    "Marks": [55, 75, 45, 85, 95, 65]
}

df = pd.DataFrame(data)

print("Student Dataset:")
print(df)

# Calculate correlation between numerical columns
correlation = df[["Study_Hours", "Marks"]].corr()

print("\nCorrelation Matrix:")
print(correlation)

# Display the correlation between study hours and marks
result = df["Study_Hours"].corr(df["Marks"])

print("\nCorrelation between Study Hours and Marks:")
print(round(result, 2))
