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
    "Company":["Microsoft","Apple","Apple","Apple","Facebook","Facebook"],
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

#IMPORTANT:
#There are multiple ways to "join" dataframes, some of them are based on...
#...keys, similar to a MySQL tables (Check online if necessary)


#------------------SHOWING RELEVANT INFO OF DATAFRAME----------------------
#Show columns of a dataframe
print("data_frame.columns =\n", data_frame.columns, "\n")

#Show rows of a dataframe
print("data_frame.index =\n", data_frame.index, "\n")

#Show overall info about the data_1frame (grouped by desired "variable")
print("data_frame.groupby('Company').describe() =")
print(data_frame.groupby('Company').describe(), "\n")



#-------------------FINDING VALUES IN DATAFRAMES--------------------------
#There are many ways to find out repeated or unique values in a dataframe
#  1)Find unique (NOT repeated) values in a column (and return them)
print("data_frame['Company'].unique() =")
print(data_frame['Company'].unique(), "\n")

#  2)Find unique values and the count of items for each
print("data_frame['Company'].value_counts() =")
print(data_frame['Company'].value_counts(), "\n")


#--------------------SORTING A DATAFRAME FROM COLUMN----------------------
#We can sort a dataframe by the values of an indicated column
print("data_frame.sort_values(by='Sales')")
print(data_frame.sort_values(by='Sales'), "\n")




#------------------APPLYING OUR FUNCTIONS TO DATAFRAME--------------------
#Let's create our own personal function to return something.
def my_function( sales ):
    #This is a random example (only to show example, doesn't make sense)
    OFFSET = 20
    TRM = 0.8
    new_sales = sales*TRM + OFFSET
    return new_sales

#If we want to apply "my_function" to a specific column of a dataframe:
#Note1 : the 'Sales' column is affected by our created function!!
#Note2 : this is powerful with lambda expression (instead of functions)
data_frame['Sales'] = data_frame['Sales'].apply( my_function )

print("data_frame (with <my_function> applied to it =")
print( data_frame )
