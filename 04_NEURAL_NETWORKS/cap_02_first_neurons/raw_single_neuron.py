# CODE FOR A SINGLE BASIC NEURON
# SANTIAGO GARCIA ARANGO

# First single neuron
inputs_1 = [2, 4, 6]
weights_1 = [0.3, 0.5, -0.1]
bias_1 = 3

output_1 = (inputs_1[0] * weights_1[0] +
            inputs_1[1] * weights_1[1] +
            inputs_1[2] * weights_1[2] + bias_1)

print("\nOUTPUT 1:\n", output_1)

# Second single neuron
inputs_2 = [2, 4, 6, 12]
weights_2 = [0.3, 0.5, -0.1, 0.3]
bias_2 = 2

output_2 = (inputs_2[0] * weights_2[0] +
            inputs_2[1] * weights_2[1] +
            inputs_2[2] * weights_2[2] +
            inputs_2[3] * weights_2[3] + bias_2)

print("\nOUTPUT 2:\n", output_2)
