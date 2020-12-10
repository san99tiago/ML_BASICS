# CODE FOR A SINGLE BASIC NEURON WITH NUMPY LIBRARY
# SANTIAGO GARCIA ARANGO

import numpy as np

# First single neuron
inputs_1 = [2, 4, 6]
weights_1 = [0.3, 0.5, -0.1]
bias_1 = 3

output_1 = np.dot(weights_1, inputs_1) + bias_1

print("\nOUTPUT 1:\n", output_1)

# Second single neuron
inputs_2 = [2, 4, 6, 12]
weights_2 = [0.3, 0.5, -0.1, 0.3]
bias_2 = 2

output_2 = np.dot(weights_2, inputs_2) + bias_2

print("\nOUTPUT 2:\n", output_2)
