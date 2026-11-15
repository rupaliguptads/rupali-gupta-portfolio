# NumPy Array Creation

import numpy as np

# Example 1: Create a one-dimensional array
numbers = np.array([10, 20, 30, 40, 50])
print("1D Array:", numbers)

# Example 2: Create a two-dimensional array
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", matrix)

# Example 3: Create an array of zeros
zeros = np.zeros(5)
print("Zeros:", zeros)

# Example 4: Create an array of ones
ones = np.ones(4)
print("Ones:", ones)

# Example 5: Create a range of numbers
sequence = np.arange(1, 11)
print("Sequence:", sequence)

# Example 6: Create evenly spaced numbers
values = np.linspace(0, 10, 5)
print("Evenly spaced values:", values)
