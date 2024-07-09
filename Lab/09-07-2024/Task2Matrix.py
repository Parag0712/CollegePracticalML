import time
import numpy as np;

# Measure the execution time for matrix multiplication using NumPy arrays vs. Python lists for a 1000x1000 matrix
numpy_matrix_1 = np.random.rand(1000, 1000)

print("Matrix 1\n",numpy_matrix_1,end="\n\n")

numpy_matrix_2 = np.random.rand(1000, 1000)
print("Matrix 2\n",numpy_matrix_1,end="\n\n")

# Now convert in list
python_list_matrix_1 = numpy_matrix_1.tolist()
# print("Python List 1\n",python_list_matrix_1,end="\n\n")

python_list_matrix_2 = numpy_matrix_2.tolist()
# print("Python List 2\n",python_list_matrix_2,end="\n\n")

start = time.time()
np.dot(numpy_matrix_1, numpy_matrix_2)
end = time.time()
numpy_time = end - start

# Here For Normal List
start = time.time()
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*python_list_matrix_2)] for X_row in python_list_matrix_1]
end = time.time()
python_time = end - start

print(f"NumPy time: {numpy_time}s, Python list time: {python_time}s")
