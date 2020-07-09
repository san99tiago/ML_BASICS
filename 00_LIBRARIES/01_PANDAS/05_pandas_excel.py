# WORK WITH CSV (AND EXCEL) FILES
# Santiago Garcia Arango, June 2020

import numpy as np
import pandas as pd
import os


# Current folder obtained with "os" library (to locate files better)
current_folder = os.path.dirname(__file__)


# Open example_csv.csv file (located at the same dir as this python file)
data_frame = pd.read_csv(os.path.join(current_folder, 'example_csv.csv'))
print("data_frame =\n", data_frame, "\n")


# Do some changes to obtained dataframe(add row with random values...)
data_frame_len = len(data_frame)
print("data_frame_len  (rows) = ", data_frame_len, "\n")

# Create a row (Series) to add to the dataframe at the last row index
cols = ["a", "b", "c", "d"]
values = np.random.randint(1, 10, size=4)

new_row = pd.Series(values, cols)
print("new_row (to add to csv) = ", new_row, "\n")

# Add row with random numbers...
data_frame = data_frame.append(new_row, ignore_index=True)
print("data_frame (with new_column added) =\n", data_frame, "\n")


# Save new example_csv.csv file (after changes of the new row added)
data_frame.to_csv(os.path.join(current_folder, 'example_csv.csv'), index=False)
