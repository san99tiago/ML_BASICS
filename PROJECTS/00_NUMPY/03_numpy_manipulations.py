#NUMPY MANIPULATIONS OF ARRAYS
#Santiago Garcia Arango
#-------------------------------------------------------------------------
import numpy as np

my_array = np.arange( 1, 11 ) # [1,2,..,8,9,10]
print( "my_array=\n", my_array, "\n")


#-----------------CHECKING CONDITIONS IN ARRAY ITEMS----------------------
#FIRST WAY...
#This is how we show boolean result of a desired condition of an array
boolean_array = my_array>5
print("my_array > 5 --> ", boolean_array, "\n")
#We can take advantage of the boolean_array, by calling the main array...
#..."evaluated" in the True statements of the boolean_array.
#This will give us only the original array where the conditions are True
print("my_array[boolean_array] = ", my_array[boolean_array], "\n")

#SECOND WAY... 
#This previous two step process is usually done in one step!!!
#Remark: This is the most common way to to this!!!
print("my_array[my_array>5] = ", my_array[my_array>5], "\n")



#-----------------------CREATE MATRICES EASIER----------------------------
#Example: create this matrix:
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 9 0 1
# 1 0 0 0 1 
# 1 1 1 1 1

cool_matrix = np.ones( (5,5) )
cool_matrix[1:4,1:4] = 0
cool_matrix[2,2] =  9
print("cool_matrix:\n", cool_matrix, "\n")


