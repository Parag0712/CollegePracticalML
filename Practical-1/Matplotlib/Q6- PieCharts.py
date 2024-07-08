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

# Design a Pie chart to represent the proportions of categorical data within a specific feature
species_counts = df_iris['species'].value_counts()
plt.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%')
plt.title('Species Proportion')
plt.show()
