#NUMPY INDEXING AND SELECTION
#Santiago Garcia Arango
#-------------------------------------------------------------------------
import numpy as np

my_array = np.arange( 0, 11 ) # [0,1,2,..,8,9,10]
print( "my_array=\n", my_array, "\n")


my_array_2d = np.array([ [5,10,15], [20,25,30], [35,40,45] ])
print( "my_array_2d=\n", my_array_2d, "\n")


#-----------------ELEMENTS OF VECTOR ARRAY MANIPULATION--------------------
#This is how we get single elements of a Numpy array
print("my_array[3] (single item of array) = ", my_array[3], "\n")

#This is how we get a part of an array
print("my_array[1:5] (part of an array) = ", my_array[1:5], "\n")


#Other way to specify part of the array
print("my_array[:6] (part of an array) = ", my_array[:6], "\n")

#Other way to specify part of the array
print("my_array[4:] (part of an array) = ", my_array[4:], "\n")


#----------------ELEMENTS OF MATRIX ARRAY MANIPULATION---------------------
#This are 2 ways to obtain a single element from a matrix [N,M] and [N,M]
print("my_array_2d[1][2] = ", my_array_2d[1][2], "\n")
print("my_array_2d[1,2] = ", my_array_2d[1,2], "\n")


#This is how we obtain a whole row from a matrix
print("my_array_2d[1] = ", my_array_2d[1], "\n")

#This is how we obtain a whole column from a matrix
print("my_array_2d[:,1] = \n", my_array_2d[:,1], "\n")


#------------------------IMPORTANT REMARK----------------------------------
#When an array is obtained from another, both of them keep connected...
#...this means that when I change one, the other changes too!!!!
#This is important to understand and keep in mind.
#To actually "copy" an array, we must do: "array.copy()" 

#Create a variable for part of an existing array (they keep connected)
part_of_array = my_array[2:7]
part_of_array[:] = 99
print("part_of_array (changed strategically) = ", part_of_array, "\n")
print("my_array (with <indirect> changes) = ", my_array, "\n")

#Remark: if we want to actually generate another array (independent array)...
#...the way to do it is by "copying" it ( array.copy() )
array_copy = my_array.copy()
print("array_copy (independent one) = ", array_copy, "\n")




