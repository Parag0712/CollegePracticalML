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
plt.figure(figsize=(10, 6))
df_iris['sepal_width'].hist(bins=20, color='skyblue', edgecolor='black')
plt.title('Sepal Width Distribution')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
