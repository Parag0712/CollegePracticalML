import matplotlib.pyplot as plt
import pandas as pd
import os

# Give Current Directory
script_dir = os.path.dirname(__file__)
iris_file_path = os.path.join(script_dir, '../', 'iris.csv')

try:
    df_iris = pd.read_csv(iris_file_path)
except FileNotFoundError:
    print("File 'iris.csv' not found. Please make sure the file exists in the current directory.")
    exit()  # Exit the script if the file is not found

# Construct histograms to analyze the distribution of numerical features in the dataset 
plt.figure(figsize=(15, 10))

# Sepal Length Distribution
plt.subplot(2, 2, 1)
df_iris['sepal_length'].hist(bins=20, color='skyblue', edgecolor='black', histtype='bar', rwidth=0.8)
plt.title('Sepal Length Distribution')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.grid(True)

# Sepal Width Distribution
plt.subplot(2, 2, 2)
df_iris['sepal_width'].hist(bins=20, color='green', edgecolor='black', histtype='bar', rwidth=0.8)
plt.title('Sepal Width Distribution')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.grid(True)

# Petal Length Distribution
plt.subplot(2, 2, 3)
df_iris['petal_length'].hist(bins=20, color='red', edgecolor='black', histtype='bar', rwidth=0.8)
plt.title('Petal Length Distribution')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.grid(True)

# Petal Width Distribution
plt.subplot(2, 2, 4)
df_iris['petal_width'].hist(bins=20, color='yellow', edgecolor='black', histtype='bar', rwidth=0.8)
plt.title('Petal Width Distribution')
plt.xlabel('Petal Width (cm)')
plt.ylabel('Frequency')
plt.grid(True)

plt.tight_layout()
plt.show()
