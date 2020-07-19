# BATCH GRADIENT DESCENT ALGORITHM
# Santiago Garcia Arango, JulY 2020

import numpy as np
import matplotlib.pyplot as plt


class GradientDescent:
    def __init__(self, alpha, X, Y, ep=0.0001, max_iterations=10000):
        """
        Gradient descent algorithm with "batch approach" for finding a
        vector theta with the parameters of a linear regression solution.
        :param alpha: constant for the learning rate.
        :param X: vector of features (it must have shape (M, N)), where M
        is the number of training examples and N is the number of features.
        :param Y: vector of target variables (outputs)
        :param ep: constant value for eps of algorithm.
        :param max_iterations: constant integer of maximum iterations.
        """

        self.X = X
        self.Y = Y
        m = self.X.shape[0]  # Number of training examples
        n = self.X.shape[1] + 1  # Number of features (X inputs)
        self.create_initial_theta(n)
        self.add_1_bias_to_X()
        self.main_loop(alpha, n, m, ep, max_iterations)

    def create_initial_theta(self, n):
        # n: the number of features given in X vector (like X inputs)
        theta = []
        for i in range(n):
            theta.append(np.random.random())
        self.theta = np.array(theta)

        self.t0 = theta[0]
        self.t1 = theta[1]

    def add_1_bias_to_X(self):
        self.X = np.c_[np.ones((len(self.X), 1)), self.X]

    def get_cost_function_J(self, m):
        # Cost function, J(theta)
        predictions = np.dot(self.X, self.theta)
        J = (1/2*m) * np.sum(np.square(predictions - self.Y))
        return J

    def main_loop(self, alpha, n, m, ep, max_iterations):
        converged = False
        J = self.get_cost_function_J(m)
        iter = 0
        while not converged:

            predictions = np.dot(self.X, self.theta)
            gradient_vector = np.dot((predictions - self.Y), self.X)
            for j in range(n):
                self.theta[j] = self.theta[j] - (alpha/m) * gradient_vector[j]

            J_new = self.get_cost_function_J(m)

            if abs(J - J_new) <= ep:
                print('Converged, iterations: ', iter, '!!!')
                converged = True

            J = J_new   # update J(theta) based on the last iteration
            iter += 1

            if iter == max_iterations:
                print('Max interactions exceeded!')
                converged = True

    def get_thetas(self):
        # return self.t0, self.t1
        return self.theta

    def plot_result(self):
        # Only for models with 1 feature (but in practice its 2 because of...
        # ... the extra first vector of ones <bias 1 vector>)
        features = self.X.shape[1]
        if features == 2:
            # Plot the training examples and the linear regression result
            for i in range(self.X.shape[0]):
                Y_predict = self.theta[0] + self.theta[1]*self.X[:, 1]

            # Create plot based on matplotlib to show linear regression
            plt.figure()
            plt.plot(self.X[:, 1], self.Y, 'o')
            plt.plot(self.X[:, 1], Y_predict, 'k')
            plt.show()


# Test found on <test_batch_gradient_descent.py>
