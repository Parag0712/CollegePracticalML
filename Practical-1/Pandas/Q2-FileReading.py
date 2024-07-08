import pandas as pd
import os 
# Load a different dataset
df_another_dataset = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
df_another_dataset.columns = ['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size']
print(df_another_dataset.head())


# Here for loca file
# Give Current Directory
script_dir = os.path.dirname(__file__)

iris_file_path = os.path.join(script_dir, '.', 'sample.txt')
# Assuming the file path is correct and the file exists in the specified location
# If the file is not found, ensure the file path is correct or the file exists in the specified location
# Load a different dataset
df_another_dataset = pd.read_csv(iris_file_path)
df_another_dataset.columns = ['product', 'price', 'quantity']
print(df_another_dataset.head())
