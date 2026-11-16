# NumPy Student Marks Analysis Project

import numpy as np

# Student names and marks in three subjects
students = np.array(["Aman", "Priya", "Rahul", "Neha", "Karan"])

marks = np.array([
    [85, 90, 88],
    [78, 82, 80],
    [92, 95, 91],
    [35, 40, 38],
    [67, 72, 70]
])

subjects = ["Maths", "Science", "English"]

print("STUDENT MARKS ANALYSIS")
print("-" * 35)

# Display each student's marks
for i in range(len(students)):
    print(students[i], ":", marks[i])

# Calculate each student's average
averages = np.mean(marks, axis=1)

print("\nStudent averages:")
for i in range(len(students)):
    print(students[i], ":", round(averages[i], 2))

# Calculate subject-wise averages
subject_averages = np.mean(marks, axis=0)

print("\nSubject averages:")
for i in range(len(subjects)):
    print(subjects[i], ":", round(subject_averages[i], 2))

# Find the highest and lowest marks
print("\nHighest mark:", np.max(marks))
print("Lowest mark:", np.min(marks))

# Identify students who passed
# Passing rule: at least 40 in every subject
passed = np.all(marks >= 40, axis=1)

print("\nPass/Fail results:")
for i in range(len(students)):
    status = "Pass" if passed[i] else "Fail"
    print(students[i], ":", status)

# Find the student with the highest average
top_index = np.argmax(averages)

print("\nTop student:", students[top_index])
print("Top average:", round(averages[top_index], 2))

# Filter students with an average of 80 or above
high_performers = students[averages >= 80]

print("\nStudents averaging 80 or above:", high_performers)
