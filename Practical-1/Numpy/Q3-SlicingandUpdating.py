import numpy as np
random_array = np.random.rand(2, 3)
print(random_array)
sliced_array = random_array[0:,0:2]

# Modify elements within an array using indexing and assignment
print("Slice Array",sliced_array);
random_array[0, 1] = 0.5  # Modify the element at index (0, 1) to 0.5
print("Random Array",random_array);
