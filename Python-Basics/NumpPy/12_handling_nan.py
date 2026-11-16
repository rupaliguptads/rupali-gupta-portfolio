# Handling Missing Values in NumPy

import numpy as np

# Example 1: Create an array containing a missing value
data = np.array([10.0, 20.0, np.nan, 40.0, 50.0])

print("Original data:", data)

# Example 2: Detect missing values
missing_values = np.isnan(data)

print("Missing value positions:", missing_values)

# Example 3: Count missing values
missing_count = np.sum(np.isnan(data))

print("Number of missing values:", missing_count)

# Example 4: Calculate mean
print("Mean with NaN:", np.mean(data))

# Example 5: Calculate mean while ignoring NaN
print("Mean ignoring NaN:", np.nanmean(data))

# Example 6: Replace NaN with zero
cleaned_data = np.nan_to_num(data, nan=0.0)

print("Data after replacing NaN:", cleaned_data)

# Example 7: Select only valid values
valid_data = data[~np.isnan(data)]

print("Valid data:", valid_data)
