# CODE FOR A SINGLE LAYER OF NEURONS USING NUMPY LIBRARY
# SANTIAGO GARCIA ARANGO

import numpy as np

def layer_of_neurons():
    """
    layer_of_neurons is a simple function to show a single layer of neurons
    using NumPy library to simplify code and get more efficient results.
    """
    inputs = [1, 2, 3, 2.5]

    weights = [[0.2, 0.8, -0.5, 1],
            [0.5, -0.91, 0.26, -0.5],
            [-0.26, -0.27, 0.17, 0.87]]

    biases = [2, 3, 0.5]

    layer_outputs = np.dot(weights, inputs) + biases

    outputs = layer_outputs

    print("\nOUTPUTS 2: {}".format(outputs))


if __name__ == "__main__":
    layer_of_neurons()

