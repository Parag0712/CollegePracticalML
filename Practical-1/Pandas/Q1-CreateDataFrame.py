import pandas as pd

# A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types.
# It is a tabular data structure, similar to an Excel spreadsheet or a table in a relational database.
# Construct a DataFrame from scratch, specifying column names and data types
# The data is a dictionary where keys are column names and values are lists of data for each column.
data = {'Column1': [1, 2, 3], 'Column2': [4, 5, 6],'Column3':[7,8,6]}

# pd.DataFrame() is used to create a DataFrame from the given data.
df = pd.DataFrame(data)

# print(df) is used to display the DataFrame.
print(df)
