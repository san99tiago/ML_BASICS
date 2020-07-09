# NUMPY OPERATIONS OF ARRAYS
# Santiago Garcia Arango, June 2020
# -------------------------------------------------------------------------
import numpy as np

my_array = np.arange(0, 11)
print("my_array = ", my_array, "\n")

# --------------------SCALAR OPERATIONS OF ARRAYS--------------------------
print("my_array + 100 = ", my_array+100, "\n")
print("my_array - 100 = ", my_array-100, "\n")
print("my_array*4 = ", my_array*4, "\n")
print("my_array/4 = ", my_array/4, "\n")

print("my_array**2 = ", my_array**2, "\n")
print("np.sqrt(my_array) = ", np.sqrt(my_array), "\n")

# ------------------BASIC OPERATIONS OF ARRAYS-----------------------------
print("my_array + my_array = ", my_array + my_array, "\n")
print("my_array - my_array = ", my_array - my_array, "\n")


# ------------------LINEAR ALGEBRA COMPUTATIONS----------------------------
print("\n\n********LINEAR ALGEBRA STUFF**********\n")
A = np.ones((2, 3))
B = np.full((3, 2), 2)
C = np.eye(3)
D = np.array([[1, 2, 3], [0, 1, 2], [1, 2, 4]])

print("A:\n", A, "\n")
print("B:\n", B, "\n")
print("C:\n", C, "\n")
print("D:\n", D, "\n")

# Get the determinant of square array
print("np.linalg.det(C) = ", np.linalg.det(C), "\n")

# Multiply matrices
print("np.matmul(A,B) =\n", np.matmul(A, B), "\n")
print("np.matmul(B,A) =\n", np.matmul(B, A), "\n")

# Inverse of a matrix
print("np.linalg.inv(D) =\n", np.linalg.inv(D), "\n")

# Eigenvalues and Eigenvectors of square array
print("np.linalg.eig(D) =\n", np.linalg.eig(D), "\n")
