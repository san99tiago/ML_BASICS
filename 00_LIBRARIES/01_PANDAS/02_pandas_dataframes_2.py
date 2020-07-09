# MULTI-INDEX DATAFRAMES IN PANDAS (AKA: "INDEX-HIGHER KEY" )
# Santiago Garcia Arango, June 2020

import numpy as np
import pandas as pd


# ---------------MULTI-INDEX DATAFRAME PANDAS--------------------
# With Pandas, we can achieve a multi-level indexing layout, where...
# ... the DataFrame has N levels of indexing. This is really usefull...
# ... when working with multiple parameters and sub-parameters of info.

# First index level (that will contain the second one)...
outside = ["G1", "G1", "G1", "G2", "G2", "G2", "G3", "G3", "G3"]  # List 1

# Second index level (that are "inside" the First index level)...
inside = [1, 2, 3, 1, 2, 3, 1, 2, 3]  # List 2


# We create the "interconnection" of these two index levels...
# Remark: this must be done in a list of tuples (to work properly)
h_index = list(zip(outside, inside))  # List of both lists (in tuples)
h_index = pd.MultiIndex.from_tuples(h_index)  # Create MultiIndex DF
print("h_index =\n", h_index, "\n")


# Now, we can go ahead and create the MultiIndex Dataframe...
data_frame = pd.DataFrame(np.random.randn(9, 3), h_index, ['A', 'B', 'C'])
print("data_frame =\n", data_frame, "\n")

# Extra/optional step (naming the index-levels)...
data_frame.index.names = ["Groups", "Numbers"]
print("data_frame (with index names) =\n", data_frame, "\n")


# -------------SEARCHING FOR MULTI-INDEX DATAFRAMES----------------
# Searching first index level...
#  1) First way of doing this (access corresponding index):
print("data_frame.loc['G1']=\n", data_frame.loc['G1'], "\n")
#  2) Second way of doing this (access cross_section of index):
print("data_frame.xs('G1')=\n", data_frame.xs('G1'), "\n")


# Searching second index level...
print("data_frame.loc['G1'].loc[1]=\n", data_frame.loc['G1'].loc[1], "\n")


# Searching general condition for a "N level" index...
# Note: will search in Any 1st level, only focusing on 2nd level condition
print("data_frame.xs(2, level='Numbers') =")
print(data_frame.xs(2, level='Numbers'))
