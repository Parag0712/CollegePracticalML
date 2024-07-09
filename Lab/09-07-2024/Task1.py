import pandas as pd
import numpy as np

# Generate a random array using numpy
random_array = np.random.rand(10, 3)

# Convert the numpy array to a pandas DataFrame
df_random = pd.DataFrame(random_array, columns=['Column1', 'Column2', 'Column3'])

print("DataFrame generated from numpy random array:\n\n", df_random)

# Constructing a DataFrame
data = {
    'Name': ['smit', 'parag', 'samarth', 'nihar'],
    'Age': [23, 20, 21, 22],
    'City': ['Junagadh', 'Talala', 'Jamnager', 'Nadiad']
}

df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
print("DataFrame created from scratch:\n\n", df)

# Adding a new row
new_data = pd.DataFrame({'Name': ['akash'], 'Age': [24], 'City': ['Surat']})
df = pd.concat([df, new_data], ignore_index=True)
print("\nDataFrame after adding new data:\n\n", df)

# Updating existing data
df.loc[df['Name'] == 'samarth', 'Age'] = 22
df.loc[df['Name'] == 'samarth', 'City'] = 'Surat'
print("\nDataFrame after updating data:\n\n", df)