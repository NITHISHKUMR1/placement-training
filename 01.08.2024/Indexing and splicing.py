import numpy as np
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]
subarray = array[1:, 1:]
print("Subarray:\n", subarray)
condition = array > 5
filtered_array = array[condition]
print("Filtered Array (values > 5):", filtered_array)
