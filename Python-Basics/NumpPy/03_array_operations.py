# NumPy Array Operations

import numpy as np

# Example 1: Arithmetic operations
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Example 2: Operations with a single number
numbers = np.array([10, 20, 30, 40])

print("Add 5:", numbers + 5)
print("Multiply by 2:", numbers * 2)

# Example 3: Comparison operations
print("Greater than 20:", numbers > 20)
print("Equal to 20:", numbers == 20)

# Example 4: Sum, minimum and maximum
print("Sum:", np.sum(numbers))
print("Minimum:", np.min(numbers))
print("Maximum:", np.max(numbers))

# Example 5: Mean and median
print("Mean:", np.mean(numbers))
print("Median:", np.median(numbers))

# Example 6: Standard deviation
print("Standard deviation:", np.std(numbers))
