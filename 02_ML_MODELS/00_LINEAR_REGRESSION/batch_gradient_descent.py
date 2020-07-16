# BATCH GRADIENT DESCENT ALGORITHM
# Algorithm based on "BogoToBogo" script found online.
# Santiago Garcia Arango, July 2020

# THIS IS A TEMPLATE... I HAVE TO UPGRADE IT AND GENERALIZE THETA...
# ... FOR A Nth DIMENSION  ARRAY!

import numpy as np
import random
import matplotlib.pyplot as plt
from scipy import stats


class GradientDescent:
    def __init__(self, alpha, x, y, ep=0.0001, max_iterations=10000):

        converged = False  #Let us stop because of epsilon or max_iterations
        m = x.shape[0]  # Number of samples to work with
        iter = 0

        # initial vector theta
        t0 = np.random.random(x.shape[1])
        t1 = np.random.random(x.shape[1])

        # total error, J(theta)
        J = sum([(t0 + t1*x[i] - y[i])**2 for i in range(m)])

        # Iterate Loop
        while not converged:
            print("theta_0 in iteration(" + str(iter) + ") = ", t0)
            print("theta_1 in iteration(" + str(iter) + ") = ", t1)
            # for each training sample, compute the gradient (d/d_theta j(theta))
            grad0 = 1.0/m * sum([(t0 + t1*x[i] - y[i]) for i in range(m)]) 
            grad1 = 1.0/m * sum([(t0 + t1*x[i] - y[i])*x[i] for i in range(m)])

            # update the theta_temp
            temp0 = t0 - alpha * grad0
            temp1 = t1 - alpha * grad1
        
            # update theta
            t0 = temp0
            t1 = temp1

            # mean squared error
            e = sum( [ (t0 + t1*x[i] - y[i])**2 for i in range(m)] ) 

            if abs(J-e) <= ep:
                print('Converged, iterations: ', iter, '!!!')
                converged = True
        
            J = e   # update error 
            iter += 1  # update iter
        
            if iter == max_iterations:
                print('Max interactions exceeded!')
                converged = True
        self.t0 = t0
        self.t1 = t1

    def get_thetas(self):
        return self.t0, self.t1


if __name__ == '__main__':

    # Get the X and Y matrices for the linear regression model
    x = [1,2,3,4,5,6,7,8,9,10]
    x = np.array(x,)
    x = x.reshape((len(x), 1))  # Same as "x.reshape(-1, 1)"
    y = [2,4,6,8,10,12,14,16,18,20]
    y = np.array(y)
    
    print(x)
    print(y)

    print('x.shape = %s y.shape = %s' %(x.shape, y.shape))

    alpha = 0.01 # learning rate
    ep = 0.01 # convergence criteria

    # call gradient decent, and get intercept(=theta0) and slope(=theta1)
    lin_model = GradientDescent(alpha, x, y, ep, max_iterations=1000)
    theta0, theta1 = lin_model.get_thetas()
    
    print('theta0 = %s theta1 = %s' %(theta0, theta1)) 

    # check with scipy linear regression 
    slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x[:,0], y)
    print('intercept = %s slope = %s' %(intercept, slope))

    # plot
    for i in range(x.shape[0]):
        y_predict = theta0 + theta1*x 

    plt.plot(x,y,'o')
    plt.plot(x,y_predict,'k-')
    plt.show()
    print("Done!")