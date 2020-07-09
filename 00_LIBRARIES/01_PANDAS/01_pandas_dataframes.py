# DATAFRAMES IN PANDAS
# Santiago Garcia Arango, June 2020

import numpy as np
import pandas as pd

# Create dataframe based on ( <DATA>, <HEADERS_VERTICAL>, <HEADERS_HORIZONTAL>)
data_frame = pd.DataFrame(
    np.random.randn(5, 4),
    ["A", "B", "C", "D", "E"],
    ["W", "X", "Y", "Z"]
    )

print("data_frame:")
print(data_frame, "\n")

# To show a determined column from the DataFrame...(it is actually a Series)
print("data_frame['W'] (COLUMN):")
print(data_frame['W'], "\n")

# To show multiple wanted columns from DataFrame...
print("data_frame[['W', 'Z']] (COLUMNS):")
print(data_frame[['W', 'Z']], "\n")

# To show a determined row from the DataFrame
# two ways:
# 1) data_frame.loc[<ROW_NAME>]
# 2) data_frame.iloc[<ROW_INDEX>]
print("data_frame.loc['A'] (ROW):")
print(data_frame.loc['A'], "\n")


# Add new column to an existing DataFrame
data_frame['NEW_COL'] = np.random.randn(5, 1)
print("data_frame (new column) :")
print(data_frame, "\n")

# To delete column, we can use "data_frame.drop(<COL_NAME>, axis=1)"
# Note: "axis=1" is to indicate that we want to delete a column.
# if we want to delete a row, then is "axis=0"

data_frame = data_frame.drop("Y", axis=1)
print("data_frame (deleted Y):")
print(data_frame, "\n")


# To show specific value, by the row and column name
print("data_frame.loc['B', 'X'] :")
print(data_frame.loc['B', 'X'], "\n")


# To evaluate conditions given in an specific dataframe (returns boolean DF)
print("data_frame > 0 :")
print(data_frame > 0, "\n")

# To show the dataframe where the condition given is true...
print("data_frame[ data_frame > 0 ] :")
print(data_frame[data_frame > 0], "\n")


# Multiple AND conditions of a dataframe in pandas (NOT with "and" operator)
# Note: for multiple conditions, we must use "&" instead of "and" !!
print("data_frame[ (data_frame['W'] > 0) & (data_frame['X'] > 0)]:\n")
print(data_frame[(data_frame['W'] > 0) & (data_frame['X'] > 0)], "\n")


# Multiple OR conditions of a dataframe in pandas (NOT with "or" operator)
# Note: for multiple or conditions, we must use "|" instead of "or" !!
print("data_frame[ (data_frame['W'] > 0) | (data_frame['X'] > 0)]:\n")
print(data_frame[(data_frame['W'] > 0) | (data_frame['X'] > 0)], "\n")
