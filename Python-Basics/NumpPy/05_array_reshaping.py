# NumPy Array Reshaping

import numpy as np

# Example 1: Create a one-dimensional array
numbers = np.array([1, 2, 3, 4, 5, 6])
print("Original array:", numbers)

# Example 2: Reshape 1D array into 2D array
matrix = numbers.reshape(2, 3)
print("2D array:")
print(matrix)

# Example 3: Reshape into 3 rows and 2 columns
matrix_2 = numbers.reshape(3, 2)
print("3 rows and 2 columns:")
print(matrix_2)

# Example 4: Find the shape of an array
print("Shape:", matrix.shape)

# Example 5: Flatten a 2D array into 1D
flat_array = matrix.flatten()
print("Flattened array:", flat_array)

# Example 6: Let NumPy calculate one dimension
matrix_3 = numbers.reshape(2, -1)
print("Reshaped using -1:")
print(matrix_3)
