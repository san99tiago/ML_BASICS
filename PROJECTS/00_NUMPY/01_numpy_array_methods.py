#METHODS AND UTILITIES OF THE NUMPY ARRAYS
#Santiago Garcia Arango
#-------------------------------------------------------------------------
import numpy as np

array_1 = np.arange(25) # Equivalent to: [0,1,2,3, ...,22, 23, 24]
array_2 = np.random.randint(0,50,10) #Vector of 5 random integers(0,50)

print("array_1:\n", array_1, "\n")
print("array_2:\n", array_2, "\n")

#----------------------RESHAPE METHOD--------------------------------------
#This method allows us to reshape an array into a given shape (must match)
new_array_1 = array_1.reshape(5,5)
print("new_array_1:\n", new_array_1, "\n")


