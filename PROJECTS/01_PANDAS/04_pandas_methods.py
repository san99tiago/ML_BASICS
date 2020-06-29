#OTHER PANDAS METHODS AND FUNCTIONALITIES
#Santiago Garcia Arango, June 2020

import numpy as np
import pandas as pd


#Dataframe 1...
data_1 = {
    "Company":["Google","Google","Microsoft","Microsoft","Facebook","Facebook"],
    "Person":["Santiago","Monica","Laura","Jaime","Lucas","Valentine"],
    "Sales":[200,120,340,124,243,350]
    }
data_frame_1 = pd.DataFrame( data_1 )
print("data_frame_1 =\n", data_frame_1, "\n")


#Dataframe 2...
data_2 = {
    "Company":["Microsoft","Apple","Apple","Apple","Google","Facebook"],
    "Person":["Sabina","Paulina","Miguel","Luis","Jorge","Gabriela"],
    "Sales":[130,215,242,117,301,234]
    }
data_frame_2 = pd.DataFrame( data_2 )
print("data_frame_2 =\n", data_frame_2, "\n")


#------------------------CONCATENATE DATAFRAMES---------------------------
#The dataframes are joined and merged in rows by default....
#Remark: if the joining is by columns, the "axis=1" must be specified
data_frame = pd.concat( [data_frame_1, data_frame_2] )
print("data_frame (concatenated) =")
print( data_frame, "\n")





#------------------SHOWING RELEVANT INFO OF DATAFRAME----------------------
#Show averall info about the data_1frame (grouped by desired "variable")
print("data_frame.groupby('Company').describe() =")
print(data_frame.groupby('Company').describe(), "\n")




