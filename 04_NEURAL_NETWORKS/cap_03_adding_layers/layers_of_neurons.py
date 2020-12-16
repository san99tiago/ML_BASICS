# CODE FOR A MULTIPLE LAYER OF NEURONS USING NUMPY LIBRARY
# SANTIAGO GARCIA ARANGO

import numpy as np


def two_layer_of_neurons():
    """
    two_layer_of_neurons is a simple function to show a double layer of
    neurons using NumPy library.
    """

    # First layer info
    inputs_1 = [[1.0, 2.0, 3.0, 2.5],
                [2.0, 5.0, -1.0, 2.0],
                [-1.5, 2.7, 3.3, -0.8]]

    weights_1 = [[0.2, 0.8, -0.5, 1],
                [0.5, -0.91, 0.26, -0.5],
                [-0.26, -0.27, 0.17, 0.87]]

    biases_1 = [2.0, 3.0, 0.5]

    # Second layer info
    weights_2 = [[0.1, -0.14, 0.5],
                [-0.5, 0.12, -0.33],
                [-0.44, 0.73, -0.13]]

    biases_2 = [-1.0, 2.0, -0.5]

    # Main layers processing
    layer_outputs_1 = np.dot(inputs_1, np.array(weights_1).T) + biases_1
    layer_outputs_2 = np.dot(layer_outputs_1, np.array(weights_2).T) + biases_2

    outputs = layer_outputs_2

    print("\nOUTPUTS :\n{}".format(outputs))


if __name__ == "__main__":
    two_layer_of_neurons()
