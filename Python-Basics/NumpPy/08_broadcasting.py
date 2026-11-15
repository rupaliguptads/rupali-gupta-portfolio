# NumPy Broadcasting

import numpy as np

# Example 1: Add a scalar to every array element
numbers = np.array([10, 20, 30, 40])
print("Original array:", numbers)
print("Add 5:", numbers + 5)

# Example 2: Multiply every element by a scalar
print("Multiply by 2:", numbers * 2)

# Example 3: Add two arrays of the same shape
first = np.array([1, 2, 3])
second = np.array([10, 20, 30])
print("Array addition:", first + second)

# Example 4: Broadcasting a 1D array across rows
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
row = np.array([10, 20, 30])

print("Matrix:\n", matrix)
print("Row:", row)
print("Matrix + row:\n", matrix + row)

# Example 5: Multiply a matrix by a scalar
print("Matrix multiplied by 3:\n", matrix * 3)
