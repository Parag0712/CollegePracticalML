import pandas as pd

# Load a different dataset
df_another_dataset = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
df_another_dataset.columns = ['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size']
print("All data")
print(df_another_dataset.head())


print("Loping")
# Perform calculations or modifications on rows or columns within the DataFrame
for index, row in df_another_dataset.iterrows():
    df_another_dataset.at[index, 'total_bill'] *= 1.1
print(df_another_dataset.head())
