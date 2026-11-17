# Pandas apply(), map(), and lambda

import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Rahul", "Priya", "Neha"],
    "Marks": [85, 62, 38, 95, 74]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Example 1: Use apply() to calculate marks out of 100
df["Percentage"] = df["Marks"].apply(lambda marks: marks)

print("\nWith Percentage Column:")
print(df)

# Example 2: Use apply() to assign grades
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"

df["Grade"] = df["Marks"].apply(calculate_grade)

print("\nWith Grades:")
print(df)

# Example 3: Use map() to convert grades into descriptions
grade_description = {
    "A": "Excellent",
    "B": "Good",
    "C": "Needs Improvement",
    "Fail": "Failed"
}

df["Performance"] = df["Grade"].map(grade_description)

print("\nWith Performance Descriptions:")
print(df)

# Example 4: Use lambda to add 5 bonus marks
df["Bonus Marks"] = df["Marks"].apply(lambda marks: marks + 5)

print("\nWith Bonus Marks:")
print(df)

# Example 5: Use apply() on a DataFrame row
df["Result"] = df["Marks"].apply(
    lambda marks: "Pass" if marks >= 40 else "Fail"
)

print("\nFinal Dataset:")
print(df)
