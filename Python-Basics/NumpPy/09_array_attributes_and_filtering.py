# NumPy Array Attributes and Boolean Filtering

import numpy as np

# Example 1: Create an array
marks = np.array([45, 78, 92, 56, 88, 35])

print("Marks:", marks)

# Example 2: Array attributes
print("Shape:", marks.shape)
print("Number of dimensions:", marks.ndim)
print("Total elements:", marks.size)
print("Data type:", marks.dtype)

# Example 3: Boolean filtering
passed_marks = marks[marks >= 40]

print("Passed marks:", passed_marks)

# Example 4: Find marks greater than 80
high_marks = marks[marks > 80]

print("Marks above 80:", high_marks)

# Example 5: Use np.where()
result = np.where(marks >= 40, "Pass", "Fail")

print("Results:", result)

# Example 6: Find unique values
numbers = np.array([10, 20, 10, 30, 20, 40])

unique_numbers = np.unique(numbers)

print("Unique numbers:", unique_numbers)
