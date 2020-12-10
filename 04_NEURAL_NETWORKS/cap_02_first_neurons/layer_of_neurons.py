# CODE FOR A SINGLE LAYER OF NEURONS
# SANTIAGO GARCIA ARANGO

def layer_of_neurons_1():
    """
    layer_of_neurons_1 is a simple function to show a single layer of neurons
    with a tedious way of applying the math involved.
    """
    inputs = [1, 2, 3, 2.5]

    weights_1 = [0.2, 0.8, -0.5, 1]
    weights_2 = [0.5, -0.91, 0.26, -0.5]
    weights_3 = [-0.26, -0.27, 0.17, 0.87]

    bias_1 = 2
    bias_2 = 3
    bias_3 = 0.5

    # Look that the inputs are "shared for all single neurons", and the ...
    # ... change is the specific weights and bias for each one
    outputs = [
        inputs[0]*weights_1[0] +
        inputs[1]*weights_1[1] +
        inputs[2]*weights_1[2] +
        inputs[3]*weights_1[3] + bias_1,

        inputs[0]*weights_2[0] +
        inputs[1]*weights_2[1] +
        inputs[2]*weights_2[2] +
        inputs[3]*weights_2[3] + bias_2,

        inputs[0]*weights_3[0] +
        inputs[1]*weights_3[1] +
        inputs[2]*weights_3[2] +
        inputs[3]*weights_3[3] + bias_3,
    ]

    print("\nOUTPUTS 1: {}".format(outputs))


def layer_of_neurons_2():
    """
    layer_of_neurons_2 is a simple function to show a single layer of neurons
    with a more "compact" way of applying the math involved.
    """
    inputs = [1, 2, 3, 2.5]

    weights = [[0.2, 0.8, -0.5, 1],
            [0.5, -0.91, 0.26, -0.5],
            [-0.26, -0.27, 0.17, 0.87]]

    biases = [2, 3, 0.5]

    # List to storage outputs of current neuron layer
    layer_outputs = []

    # Go through each neuron (weights and biases must match in size)
    for neuron_weights, neuron_bias in zip(weights, biases):
        # Every current neuron output
        neuron_output = 0

        # For each input and weight to the current neuron
        for n_input, weight in zip(inputs, neuron_weights):
            # Multiply each input to its weight and add to neuron's output
            neuron_output += n_input*weight

        # After the main sum_product is done, add the bias
        neuron_output += neuron_bias

        # Add neuron's current result to the layer's output list
        layer_outputs.append(neuron_output)

    outputs = layer_outputs

    print("\nOUTPUTS 2: {}".format(outputs))


if __name__ == "__main__":
    # Show tests for both functions (the tedious and the compact one)
    layer_of_neurons_1()
    layer_of_neurons_2()
