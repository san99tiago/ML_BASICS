# TEST ON BATCH GRADIENT DESCENT ALGORITHM
# Santiago Garcia Arango, July 2020

import batch_gradient_descent
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# Get the X and Y matrices for the linear regression model
X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
X = np.array(X)
X = X.reshape((len(X), 1))  # Same as "x.reshape(-1, 1)"

Y = [2, 4, 6, 8, 11.7, 12, 14, 16, 18, 18.3, 22, 24, 26, 28,
        30.9, 32, 34, 36, 38, 40.7]
Y = np.array(Y)

# print("X = ", X)
# print("Y = ", Y)
print("X.shape = {}  Y.shape = {}".format(X.shape, Y.shape))

alpha = 0.00001  # Learning rate for gradient of Cost function J(theta)
ep = 0.01  # Convergence criteria
iterations = 10000  # Max number of iterations

# Call gradient decent, and get the resulting theta vector for parameters
lin_model = batch_gradient_descent.GradientDescent(
    alpha,
    X,
    Y,
    ep,
    max_iterations=iterations
    )
theta = lin_model.get_thetas()
lin_model.plot_result()
print("theta[0] = {}\ntheta[1] = {}".format(theta[0], theta[1]))

# Check with scipy best linear regression possible (to compare)
slope, intercept, r_value, p_value, sl_std_er = stats.linregress(X[:, 0], Y)
print("intercept = {}\nslope = {}".format(intercept, slope))
Y_from_scipy = intercept + slope*X

plt.figure()
plt.plot(X, Y, 'o')
plt.plot(X, Y_from_scipy)
plt.show()
