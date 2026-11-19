# EDA Project - Step 7
# Outlier Detection Using IQR

import pandas as pd

data = {
    "Student": ["Aman", "Riya", "Rahul", "Neha", "Priya", "Karan", "Simran"],
    "Marks": [75, 82, 78, 90, 85, 80, 150]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Calculate the first and third quartiles
Q1 = df["Marks"].quantile(0.25)
Q3 = df["Marks"].quantile(0.75)

# Calculate the Interquartile Range
IQR = Q3 - Q1

# Calculate the lower and upper limits
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

print("\nQ1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

# Identify outliers
outliers = df[
    (df["Marks"] < lower_limit) |
    (df["Marks"] > upper_limit)
]

print("\nDetected Outliers:")
print(outliers)
