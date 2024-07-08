# Shape Manipulation:
# o Reshape an array into different dimensions (e.g., from 1D to 2D).
# o Transpose an array to swap rows and columns.

import numpy as np
sequence_array = np.arange(0, 30)

print(sequence_array);

# Reshape an array into different dimensions (e.g., from 1D to 2D)
# The reshape method takes a tuple of integers as an argument, specifying the new shape of the array.
# The -1 in the tuple means that the size of that dimension is calculated automatically.
# reshaped_array = sequence_array.reshape(-1, 3, 2)
reshaped_array = sequence_array.reshape(-1, 6)
print("Reshape array\n",reshaped_array,end="\n\n");

# # Transpose an array to swap rows and columns
transposed_array = reshaped_array.T
print("Transposed array\n", transposed_array)
