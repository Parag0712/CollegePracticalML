import matplotlib.pyplot as plt
import pandas as pd
import os

# Give Current Directory
script_dir = os.path.dirname(__file__)
iris_file_path = os.path.join(script_dir, '.', 'iris.csv')

try:
    df_iris = pd.read_csv(iris_file_path)
except FileNotFoundError:
    print("File 'iris.csv' not found. Please make sure the file exists in the current directory.")

# Convert non-numeric columns to numeric before calculating the correlation matrix
df_iris = df_iris.apply(lambda x: pd.to_numeric(x, errors='coerce') if pd.api.types.is_string_dtype(x) else x)

# Calculate the correlation matrix
correlation_matrix = df_iris.corr()

# Plotting the correlation matrix
plt.figure(figsize=(10, 8))
plt.matshow(correlation_matrix)
plt.colorbar()
plt.show()
