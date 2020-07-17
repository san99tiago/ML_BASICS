# BATCH GRADIENT DESCENT ALGORITHM
# Algorithm based on "BogoToBogo" script found online.
# Santiago Garcia Arango, JulY 2020

# THIS IS A TEMPLATE... I HAVE TO UPGRADE IT AND GENERALIZE THETA...
# ... FOR A Nth DIMENSION  ARRAY!
#   https://towardsdatascience.com/gradient-descent-in-pYthon-a0d07285742f

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


class GradientDescent:
    def __init__(self, alpha, X, Y, ep=0.0001, max_iterations=10000):

        converged = False

        self.X = X
        self.Y = Y
        m = X.shape[0]  # Number of training examples
        n = X.shape[1] + 1  # Number of features (X inputs)
        self.create_initial_theta(n)
        self.add_1_bias_to_X()

        J = self.get_cost_function_J()


        t0 = self.t0
        t1 = self.t1

        iter = 0
        while not converged:

            predictions = np.dot(self.X, self.theta)
            gradient_vector = np.dot((predictions - self.Y), self.X)
            for j in range(n):
                self.theta[j] = self.theta[j] - alpha*gradient_vector[j]

            print("MY_THETA = ", self.theta)
            print("GOOD_THETA = ", t0, t1)


            predictions = np.dot(self.X, self.theta)
            J_new = (1/2) * np.sum(np.square(predictions - self.Y))
            print("J_new = ", J_new)
            

            if abs(J-J_new) <= ep:
                print('Converged, iterations: ', iter, '!!!')
                converged = True
        
            J = J_new   # update J(theta) based on the last iteration
            iter += 1  # update iter
        
            if iter == max_iterations:
                print('Max interactions exceeded!')
                converged = True
        self.t0 = t0
        self.t1 = t1
        self.theta

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
        print(self.X)

    def get_cost_function_J(self):
        # Cost function, J(theta)
        predictions = np.dot(self.X, self.theta)
        J = (1/2) * np.sum(np.square(predictions - self.Y))
        return J

    def get_thetas(self):
        # return self.t0, self.t1
        return self.theta











if __name__ == '__main__':

    # Get the X and Y matrices for the linear regression model
    X = [1,2,3,4.5,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    X = np.array(X,)
    X = X.reshape((len(X), 1))  # Same as "x.reshape(-1, 1)"
    Y = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40]
    Y = np.array(Y)
    
    print(X)
    print(Y)

    print('X.shape = %s Y.shape = %s' %(X.shape, Y.shape))

    alpha = 0.00001 # learning rate
    ep = 0.01 # convergence criteria
    iterations = 1000

    # call gradient decent, and get intercept(=theta0) and slope(=theta1)
    lin_model = GradientDescent(alpha, X, Y, ep, max_iterations=iterations)
    theta = lin_model.get_thetas()
    
    print('theta0 = %s theta1 = %s' %(theta[0], theta[1])) 

    # check with scipy linear regression 
    slope, intercept, r_value, p_value, slope_std_error = stats.linregress(X[:,0], Y)
    print('intercept = %s slope = %s' %(intercept, slope))
    Y_from_scipy = intercept + slope*X

    # plot
    for i in range(X.shape[0]):
        Y_predict = theta[0] + theta[1]*X 

    plt.figure()
    plt.plot(X,Y,'o')
    plt.plot(X,Y_predict,'k-')

    plt.figure()
    plt.plot(X,Y,'o')

    plt.plot(X,Y_from_scipy)
    plt.show()
    print("Done!")