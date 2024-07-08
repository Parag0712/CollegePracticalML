import pandas as pd
import os 
# Load a different dataset
df_another_dataset = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
df_another_dataset.columns = ['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size']
print("all data")
print(df_another_dataset.head())

print("\n\nSpecific row and colums")
# Select specific rows and columns using various indexing methods
selected_rows = df_another_dataset.iloc[0:10, [0, 1]]
print(selected_rows)


# Using Function
print("\n\nSpecific row and colums")
# Select specific rows and columns using various indexing methods
print(df_another_dataset.loc[0:5, ['total_bill', 'tip']])


print("\n\nfilter data")
# Filter data based on specific conditions using boolean expressions
print(df_another_dataset[df_another_dataset['total_bill'] > 32])