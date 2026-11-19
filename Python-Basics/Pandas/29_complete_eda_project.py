# Complete EDA Project
# Step 1: Dataset Creation and Initial Inspection

import pandas as pd

data = {
    "Student": ["Aman", "Riya", "Rahul", "Neha", "Priya",
                "Karan", "Simran", "Arjun", "Pooja", "Vikas"],
    "Age": [20, 21, 19, 22, 20, 21, 20, 23, 19, 22],
    "Study_Hours": [2, 4, 1, 5, 6, 3, 4, 2, 5, 3],
    "Marks": [55, 75, 45, 85, 95, 65, 90, 60, 88, 72],
    "City": ["Delhi", "Mumbai", "Delhi", "Jaipur", "Mumbai",
             "Jaipur", "Delhi", "Pune", "Mumbai", "Pune"]
}

df = pd.DataFrame(data)

print("===== DATASET OVERVIEW =====")

print("\nFirst Five Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
df.info()

print("\nStatical Summary:")
print(df.describe())

# Step 2: Data Quality Checks

print("\n===== DATA QUALITY CHECKS =====")

# Check missing values in each column
print("\nMissing Values by Column:")
print(df.isnull().sum())

# Count all missing values
print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

# Check duplicate rows
print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())

# Check data types
print("\nColumn Data Types:")
print(df.dtypes)

# Check for duplicate student names
print("\nDuplicate Student Names:")
print(df[df["Student"].duplicated()])istical Summary:")
print(df.describe())

# Step 3: Handle Missing Values

print("\n===== MISSING VALUE HANDLING =====")

# Create a copy for cleaning
df_cleaned = df.copy()

# Introduce missing values for practice
df_cleaned.loc[2, "Age"] = None
df_cleaned.loc[4, "Marks"] = None
df_cleaned.loc[6, "City"] = None

print("\nMissing Values Before Cleaning:")
print(df_cleaned.isnull().sum())

# Fill missing Age with the median
df_cleaned["Age"] = df_cleaned["Age"].fillna(
    df_cleaned["Age"].median()
)

# Fill missing Marks with the mean
df_cleaned["Marks"] = df_cleaned["Marks"].fillna(
    df_cleaned["Marks"].mean()
)

# Fill missing City with the most frequent city
df_cleaned["City"] = df_cleaned["City"].fillna(
    df_cleaned["City"].mode()[0]
)

print("\nDataset After Cleaning:")
print(df_cleaned)

print("\nMissing Values After Cleaning:")
print(df_cleaned.isnull().sum())

# Step 4: Duplicate Record Analysis

print("\n===== DUPLICATE RECORD ANALYSIS =====")

# Create a copy for duplicate analysis
df_deduplicated = df_cleaned.copy()

# Add a duplicate row for practice
df_deduplicated = pd.concat(
    [df_deduplicated, df_deduplicated.iloc[[0]]],
    ignore_index=True
)

print("\nRows Before Removing Duplicates:")
print(len(df_deduplicated))

# Count duplicate rows
print("\nNumber of Duplicate Rows:")
print(df_deduplicated.duplicated().sum())

# Display duplicate records
print("\nDuplicate Records:")
print(df_deduplicated[df_deduplicated.duplicated()])

# Remove duplicate rows
df_deduplicated = df_deduplicated.drop_duplicates()

print("\nRows After Removing Duplicates:")
print(len(df_deduplicated))

print("\nDuplicates Remaining:")
print(df_deduplicated.duplicated().sum())

# Step 5: Outlier Detection Using IQR

print("\n===== OUTLIER DETECTION =====")

# Use the cleaned dataset for analysis
Q1 = df_deduplicated["Marks"].quantile(0.25)
Q3 = df_deduplicated["Marks"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

print("\nFirst Quartile (Q1):", Q1)
print("Third Quartile (Q3):", Q3)
print("Interquartile Range (IQR):", IQR)

print("\nLower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

# Identify outliers
outliers = df_deduplicated[
    (df_deduplicated["Marks"] < lower_limit) |
    (df_deduplicated["Marks"] > upper_limit)
]

print("\nDetected Outliers:")
if outliers.empty:
    print("No outliers detected.")
else:
    print(outliers[["Student", "Marks"]])

# Step 6: Correlation Analysis

print("\n===== CORRELATION ANALYSIS =====")

# Calculate correlations between numerical columns
correlation = df_deduplicated[
    ["Age", "Study_Hours", "Marks"]
].corr()

print("\nCorrelation Matrix:")
print(correlation.round(2))

# Check the relationship between study hours and marks
study_marks_corr = df_deduplicated[
    "Study_Hours"
].corr(df_deduplicated["Marks"])

print("\nCorrelation Between Study Hours and Marks:")
print(round(study_marks_corr, 2))

# Step 7: Grouped Analysis and Key Insights

print("\n===== GROUPED ANALYSIS =====")

# Calculate average marks by city
city_average = df_deduplicated.groupby("City")["Marks"].mean()

print("\nAverage Marks by City:")
print(city_average.round(2))

# Calculate multiple statistics for each city
city_summary = df_deduplicated.groupby("City")["Marks"].agg(
    ["count", "mean", "min", "max"]
)

print("\nCity-wise Performance Summary:")
print(city_summary.round(2))

# Identify the city with the highest average marks
top_city = city_average.idxmax()

print("\nCity with Highest Average Marks:", top_city)
print("Highest City Average:", round(city_average.max(), 2))

# Identify the top-performing student
top_student_index = df_deduplicated["Marks"].idxmax()
top_student = df_deduplicated.loc[top_student_index]

print("\nTop-Performing Student:")
print(top_student[["Student", "City", "Marks"]])

# Step 8: EDA Visualizations

import matplotlib.pyplot as plt

print("\n===== CREATING EDA VISUALIZATIONS =====")

# Create three charts
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Chart 1: Distribution of student marks
axes[0].hist(
    df_deduplicated["Marks"],
    bins=5,
    edgecolor="black"
)
axes[0].set_title("Distribution of Marks")
axes[0].set_xlabel("Marks")
axes[0].set_ylabel("Number of Students")

# Chart 2: Average marks by city
city_average = df_deduplicated.groupby("City")["Marks"].mean()

axes[1].bar(city_average.index, city_average.values)
axes[1].set_title("Average Marks by City")
axes[1].set_xlabel("City")
axes[1].set_ylabel("Average Marks")
axes[1].tick_params(axis="x", rotation=30)

# Chart 3: Study hours vs marks
axes[2].scatter(
    df_deduplicated["Study_Hours"],
    df_deduplicated["Marks"]
)
axes[2].set_title("Study Hours vs Marks")
axes[2].set_xlabel("Study Hours")
axes[2].set_ylabel("Marks")

plt.tight_layout()
plt.show()

