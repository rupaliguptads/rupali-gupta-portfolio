# NumPy Matrix Operations

import numpy as np

# Example 1: Create two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Example 2: Element-wise multiplication
print("Element-wise multiplication:\n", A * B)

# Example 3: Matrix multiplication using np.dot()
print("Matrix multiplication using dot():\n", np.dot(A, B))

# Example 4: Matrix multiplication using @
print("Matrix multiplication using @:\n", A @ B)

# Example 5: Transpose a matrix
print("Transpose of A:\n", A.T)

# Example 6: Sum of all elements
print("Total sum of A:", np.sum(A))

# Example 7: Sum of each column
print("Column sums:", np.sum(A, axis=0))

# Example 8: Sum of each row
print("Row sums:", np.sum(A, axis=1))
