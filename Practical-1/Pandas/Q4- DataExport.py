import pandas as pd

# Load a different dataset
df_another_dataset = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
df_another_dataset.columns = ['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size']
print("All data")
print(df_another_dataset.head())

print("\n\nFiltered data")

# Filter data based on specific conditions using boolean expressions
filtered_df = df_another_dataset[df_another_dataset['total_bill'] > 32]
print(filtered_df)
# Export the filtered data to a new CSV file
filtered_df.to_csv('filtered_tips.csv', index=False)
print("\n\nFiltered data from CSV file")
print(filtered_df)
