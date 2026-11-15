# NumPy Random Numbers

import numpy as np

# Example 1: Generate a random number
random_number = np.random.randint(1, 101)
print("Random number:", random_number)

# Example 2: Generate 5 random integers
random_numbers = np.random.randint(1, 51, size=5)
print("Five random integers:", random_numbers)

# Example 3: Generate random decimal numbers
decimal_numbers = np.random.rand(5)
print("Random decimal numbers:", decimal_numbers)

# Example 4: Generate a 2D array of random integers
random_array = np.random.randint(1, 20, size=(3, 3))
print("Random 2D array:\n", random_array)

# Example 5: Set a seed for reproducible results
np.random.seed(42)
print("Repeatable random numbers:", np.random.randint(1, 101, size=5))
