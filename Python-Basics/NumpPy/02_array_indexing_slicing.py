# NumPy Array Indexing and Slicing

import numpy as np

# Example 1: Access elements using index
numbers = np.array([10, 20, 30, 40, 50])

print("First element:", numbers[0])
print("Third element:", numbers[2])
print("Last element:", numbers[-1])

# Example 2: Access a range of elements
print("Elements from index 1 to 3:", numbers[1:4])
print("First three elements:", numbers[:3])
print("Last two elements:", numbers[-2:])

# Example 3: Change an array element
numbers[1] = 99
print("Updated array:", numbers)

# Example 4: Indexing in a 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6]])

print("Element at row 0, column 1:", matrix[0, 1])
print("Second row:", matrix[1])
print("First column:", matrix[:, 0])

# Example 5: Slice a 2D array
print("First row, first two columns:")
print(matrix[0, :2])
