# USEFUL METHODS OF THE NUMPY ARRAYS
# Santiago Garcia Arango, June 2020
# -------------------------------------------------------------------------
import numpy as np

array_1 = np.arange(25)  # Equivalent to: [0,1,2,3, ...,22, 23, 24]
array_2 = np.random.randint(0, 50, 10)  # Vector of 5 random integers(0,50)

print("array_1:\n", array_1, "\n")
print("array_2:\n", array_2, "\n")


# ----------------------RESHAPE METHOD--------------------------------------
# This method allows us to reshape an array into a given shape (must match)
# Remark: the product of dimensions N*M must be equal to the size of vector
new_array_1 = array_1.reshape(5, 5)
print("array_1 (reshaped):\n", new_array_1, "\n")


# -------------------------GET SHAPE OF ARRAY------------------------------
print("SHAPE(array_1) -->", array_1.shape)
print("SHAPE(array_1 (reshaped) ) -->", new_array_1.shape)
print("SHAPE(array_2) -->", array_2.shape, "\n")


# -------------------MAXIMUM AND MINIMUM OF ARRAY---------------------------
# array.max(): returns the max VALUE of a given array
# array.min(): returns the min VALUE of a given array
# array.argmax(): returns INDEX location of the max VALUE of given array
# array.argmin(): returns INDEX location of the min VALUE of given array
print("MAX(array_2) =", array_2.max(), " (at index", array_2.argmax(), ")\n")
print("MIN(array_2) =", array_2.min(), " (at index", array_2.argmin(), ")\n")


# ------------------------DATATYPE OF ARRAY----------------------------------
print("DATATYPE(array_1) -->", array_1.dtype)
print("DATATYPE(array_2) -->", array_2.dtype)
