# NumPy Two-Dimensional Arrays

import numpy as np

# Example 1: Create a 2D array
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("2D Array:")
print(matrix)

# Example 2: Access an element
print("First row, second column:", matrix[0, 1])

# Example 3: Access a complete row
print("First row:", matrix[0])

# Example 4: Access a complete column
print("Second column:", matrix[:, 1])

# Example 5: Find number of rows and columns
print("Shape:", matrix.shape)
print("Number of dimensions:", matrix.ndim)

# Example 6: Calculate sum by columns and rows
print("Column sums:", np.sum(matrix, axis=0))
print("Row sums:", np.sum(matrix, axis=1))
