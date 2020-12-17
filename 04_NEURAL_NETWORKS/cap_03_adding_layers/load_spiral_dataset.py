# CODE FOR LOAD AND USAGE OF DATA WITH NNFS PACKAGE
# SANTIAGO GARCIA ARANGO

import nnfs
import numpy as np
import matplotlib.pyplot as plt
from nnfs.datasets import spiral_data

# Initialize Neural Networks From Scratch package for following the book
nnfs.init(dot_precision_workaround=True, default_dtype='float32', random_seed=0)

# Create main data spiral from NNFS package
X, y = spiral_data(samples=100, classes=3)

# Generate an uncolored 100 samples and 3 classes spiral (and plot)
plt.figure()
plt.scatter(X[:, 0], X[:, 1])
plt.title("Uncolored spiral dataset")

# Generate a colored 100 samples and 3 classes spiral (and plot)
plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=y, cmap="brg")
plt.title("Colored spiral dataset")
plt.show()
