import pandas as pd

# Load a different dataset
df_another_dataset = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
df_another_dataset.columns = ['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size']
print("All data")
print(df_another_dataset.head())

print("Masking")
# Create a mask for the data
mask = (df_another_dataset['total_bill'] > 32)
# Apply the mask to the data
masked_data = df_another_dataset[mask]
print("Masked data:")
print(masked_data)
