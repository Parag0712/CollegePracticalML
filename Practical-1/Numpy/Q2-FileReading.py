import numpy as np
import os;

# Give Current Directory
script_dir = os.path.dirname(__file__)

iris_file_path = os.path.join(script_dir, '.', 'sample.txt')
# Assuming the file path is correct and the file exists in the specified location
# If the file is not found, ensure the file path is correct or the file exists in the specified location
try:
    iris_data = np.genfromtxt(iris_file_path, delimiter=',', dtype=None, encoding=None)
    print(iris_data)
except FileNotFoundError:
    print("File 'iris.txt' not found. Please check the file path or ensure the file exists.")