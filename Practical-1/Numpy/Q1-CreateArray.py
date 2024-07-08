import numpy as np;

# Create a NumPy array with zeros, ones, and random values.
zeros_array = np.zeros((1, 3))
print("Zero Array", zeros_array)


ones_array = np.ones((1, 3))
print("Once Array",ones_array)
random_array = np.random.rand(3, 3)

# Generate an array with a specific sequence of numbers (e.g., arithmetic progression)
# In this case, start=0, stop=30, and step=5.
sequence_array = np.arange(0, 30, 5)

print("Sequence Array",sequence_array)