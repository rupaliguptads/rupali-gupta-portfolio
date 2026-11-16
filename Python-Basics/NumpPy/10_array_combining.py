# NumPy Array Combining

import numpy as np

# Example 1: Create two arrays
array1 = np.array([10, 20, 30])
array2 = np.array([40, 50, 60])

print("Array 1:", array1)
print("Array 2:", array2)

# Example 2: Concatenate arrays
combined = np.concatenate((array1, array2))

print("Concatenated array:", combined)

# Example 3: Stack arrays vertically
vertical_stack = np.stack((array1, array2), axis=0)

print("Vertical stack:\n", vertical_stack)

# Example 4: Stack arrays horizontally
horizontal_stack = np.stack((array1, array2), axis=1)

print("Horizontal stack:\n", horizontal_stack)

# Example 5: Combine 2D arrays
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

combined_2d = np.concatenate((a, b), axis=0)

print("Combined 2D arrays:\n", combined_2d)

# Example 6: Combine columns
combined_columns = np.concatenate((a, b), axis=1)

print("Combined columns:\n", combined_columns)
