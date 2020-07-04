#HOW TO HANDLE MISSING DATA IN PANDAS
#Santiago Garcia Arango, June 2020

import numpy as np
import pandas as pd

#Create a dictionary with missing values (to show missing data examples)
dictionary = {
    "A":[1,2,np.nan,5],
    "B":[5,np.nan,np.nan,2],
    "C":[1,2,3,4],
    "D":[3,np.nan,3,5]
    }

#Create data_frame from the dictionary already created
data_frame = pd.DataFrame( dictionary )
print( "data_frame=\n", data_frame, "\n")

#----------------METHOD 1(delete rows/columns with NAN)----------------------
#1) Delete rows that have NAN values from the data_frame.
print("data_frame.dropna() [delete NAN rows]=")
print( data_frame.dropna(), "\n")

#2) Delete columns that have NAN values from the data_frame.
print("data_frame.dropna(axis=1) [delete NAN rows]=")
print( data_frame.dropna(axis=1), "\n")



#---------------------------METHOD 2(fill the NAN)--------------------------
#Get the average(or mean) value of each data_frame column
average_1 = data_frame.mean()
print("average_1 (COLUMNS average)=\n", average_1, "\n" )

#We can strategically fill the missing values (NAN) with the average value
print("data_frame.fillna(value=average_1)=")
print(data_frame.fillna(value=average_1), "\n")

