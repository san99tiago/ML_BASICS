# BATCH GRADIENT DESCENT ALGORITHM
# Santiago Garcia Arango, July 2020

import numpy as np
import matplotlib.pyplot as plt


class GradientDescent:
    def __init__(self, alpha, X, y, ep=0.0001, max_iterations=10000):
        """
        Gradient descent algorithm with "batch approach" for finding a
        vector theta with the parameters of a linear regression solution.
        :param alpha: constant for the learning rate.
        :param X: vector of features (it must have shape (M, N)), where M
        is the number of training examples and N is the number of features.
        :param y: vector of target variables (outputs)
        :param ep: constant value for eps of algorithm.
        :param max_iterations: constant integer of maximum iterations.
        """

        self.X = X  # X.shape = (M, N), but will become (M, N+1)
        self.y = y  # y.shape = (M, 1)
        m = self.X.shape[0]  # Number of training examples
        n = self.X.shape[1]  # Number of features (X inputs)
        self.create_initial_theta(n)
        self.add_1_bias_to_X()
        self.main_loop(alpha, n, m, ep, max_iterations)

    def create_initial_theta(self, n):
        # n: the number of features given in X vector (like X inputs)
        theta = []
        for i in range(n+1):
            theta.append(np.random.random())
        self.theta = np.array(theta)

    def add_1_bias_to_X(self):
        # Add extra column of "1" bias to self.X vector...
        self.X = np.c_[np.ones((len(self.X), 1)), self.X]

    def get_cost_function_J(self, m):
        # Cost function, J(theta)
        predictions = np.dot(self.X, self.theta)
        J = (1/2*m) * np.sum(np.square(predictions - self.y))
        return J

    def main_loop(self, alpha, n, m, ep, max_iterations):
        converged = False
        J = self.get_cost_function_J(m)
        iter = 0
        while not converged:
            # Some dimensional analysis to make sure we are ok:
            # -->self.y.shape = (M, 1)
            # -->predictions.shape = (M, 1) (also known as hypothesis)
            # -->self.X.T.shape = (N+1, M)
            # -->gradient_vector.size = (N+1, 1)

            predictions = np.dot(self.X, self.theta)
            gradient_vector = np.dot(self.X.T, (predictions - self.y))

            self.theta = self.theta - (alpha/m) * gradient_vector

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
        return self.theta

    def plot_result(self):
        # Only for models with 1 feature (but in practice its 2 because of...
        # ... the extra first vector of ones <bias 1 vector>)
        features = self.X.shape[1]
        if features == 2:
            # Plot the training examples and the linear regression result
            for i in range(self.X.shape[0]):
                y_predict = self.theta[0] + self.theta[1]*self.X[:, 1]

            # Create plot based on matplotlib to show linear regression
            plt.figure()
            plt.plot(self.X[:, 1], self.y, 'o')
            plt.plot(self.X[:, 1], y_predict, 'k')
            plt.show()


# Test found on <test_batch_gradient_descent.py>
