# CODE FOR A DENSE LAYER OF NEURONS CLASS USING NUMPY
# SANTIAGO GARCIA ARANGO

import numpy as np
import nnfs
import matplotlib.pyplot as plt
from nnfs.datasets import spiral_data

# Initialize Neural Networks From Scratch package for following the book
nnfs.init(dot_precision_workaround=True, default_dtype='float32', random_seed=0)


class DenseLayer:
    """
    DenseLayer is a class to create and process generalized neuron layers.
    :param n_inputs: number of inputs
    :param n_neurons: number of neurons
    """
    def __init__(self, n_inputs, n_neurons):
        # Initialize main layer with random weights and zero vector for biases
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        # Apply main forward pass with
        self.output = np.dot(inputs, self.weights) + self.biases


if __name__ == "__main__":
    # --------------- TEST FORWARD PASS WITH MY NEW CLASS --------------
    # Create dataset
    # 2D spiral size(X)=(samples*classes, 2) and size(y)=(samples*classes, 1)
    # Spiral has two features in the 2D plane and specific "classes" as output
    X, y = spiral_data(samples=100, classes=3)

    print("\n\n---------------- MY DATASET -----------------\n")
    print("shape(X):", np.shape(X), "... main training features\n")
    print("shape(y):", np.shape(y), "... output for each set of features\n")

    # Create dense layer with given "input features" and "output values"
    dense_1 = DenseLayer(2, 3)

    print("\n\n--------- DENSE LAYER INITIALIZING ----------\n")
    print("shape(dense_1.weights):", np.shape(dense_1.weights), "\n")
    print("shape(dense_1.biases):", np.shape(dense_1.biases), "\n")

    # Perform a forward pass of our training data through this layer
    dense_1.forward(X)

    # See output of the first samples
    print("\n\n--------- FORWARD PASS ----------\n *Only some of them...\n")
    print(dense_1.output[:5])

    # Visualize dataset graphically
    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap="brg")
    plt.title("Santi's spiral dataset")
    plt.show()
