# SERIES WITH PANDAS
# Santiago Garcia Arango, June 2020

import numpy as np
import pandas as pd

# ----------------UNDERSTANDING SERIES IN PANDAS--------------------------
# Basic information to play with pandas
my_labels = ["A", "B", "C"]
my_data = [10, 20, 30]
my_array = np.array(my_data)
my_dict = {"A": 10, "B": 20, "C": 30}
print("my_labels = ", my_labels)
print("my_data = ", my_data)
print("my_array = ", my_array)
print("my_dict = ", my_dict, "\n")

# We create different versions of Series, based on the parameters
# note: we can pass lists, arrays as "data" or even dictionaries
series_1 = pd.Series(data=my_data)
series_2 = pd.Series(data=my_array)
series_3 = pd.Series(data=my_data, index=my_labels)
series_4 = pd.Series(data=my_array, index=my_labels)
series_5 = pd.Series(my_dict)

print("series_1 =\n", series_1, "\n")
print("series_2 =\n", series_2, "\n")
print("series_3 =\n", series_3, "\n")
print("series_4 =\n", series_4, "\n")
print("series_5 =\n", series_5, "\n")


# -------------------EXAMPLE WITH SERIES----------------------------------
# The correct way to pass arguments is (<DATA>, <INDEX>)
series_countries_1 = pd.Series([1, 2, 3, 4], ["COL", "USA", "FRA", "GER"])
series_countries_2 = pd.Series(["COL", "USA", "FRA", "GER"], [1, 2, 3, 4])

print("series_countries_1 = \n", series_countries_1, "\n")
print("series_countries_2 = \n", series_countries_2, "\n")


# To access the Series, it is similar to a python dictionary
print("series_countries_1['USA'] = ", series_countries_1["USA"], "\n")
print("series_countries_2[1] = ", series_countries_2[1], "\n")
