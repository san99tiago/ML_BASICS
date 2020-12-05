# TEST ON BATCH GRADIENT DESCENT ALGORITHM
# Santiago Garcia Arango, July 2020

import batch_gradient_descent
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import os


def get_data():
    # Lets try to import our own dataset (otherwise create a default one)
    try:
        # Current folder obtained with "os" library (to locate files better)
        current_folder = os.path.dirname(__file__)

        data_frame = pd.read_excel(
            os.path.join(current_folder, "data.xlsx"),
            sheet_name = "Sheet1"
            )

        # Create the "X" and "y" vectors for the model based on data_frame
        X = np.array(data_frame[["size(m^2)", "bedrooms"]])
        y = np.array(data_frame["price(millions_COP)"])

        print("\nX =\n", X)
        print("\ny =\n", y)

        return X, y

    except:
        print("THE DATA_FILE COULDN'T BE OPENED.")
        print("CHECK <get_data()> function")
        # Get the X and y matrices for the linear regression model
        X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        X = np.array(X)
        X = X.reshape((len(X), 1))  # We reshape it so it becomes "2D"

        y = [2, 4, 6, 8, 11.7, 12, 14, 16, 18, 18.3, 22, 24, 26, 28,
                30.9, 32, 34, 36, 38, 40.7]
        y = np.array(y)

        return X, y


def run_test(alpha, X, y, ep, iterations):
    # Call gradient decent, and get the resulting theta vector for parameters
    lin_model = batch_gradient_descent.GradientDescent(
        alpha,
        X,
        y,
        ep,
        max_iterations=iterations
        )

    theta = lin_model.theta
    for n in range(len(theta)):
        print("theta[", str(n), "] = ", theta[n])
    # print("theta[0] = {}\ntheta[1] = {}".format(theta[0], theta[1]))

    J_history = lin_model.J_history
    # print("J_history = ", J_history)

    lin_model.plot_result()

    plt.figure()
    plt.plot(np.arange(len(J_history)), J_history, 'o')


def check_real_output(X, y):
    # Check with scipy best linear regression possible (to compare)
    slope, intercept, r_value, p_value, sl_std_er = stats.linregress(X[:, 0], y)
    print("intercept = {}\nslope = {}".format(intercept, slope))
    y_from_scipy = intercept + slope*X

    plt.figure()
    plt.plot(X, y, 'o')
    plt.plot(X, y_from_scipy)
    plt.show()


# ------------------RUN THE TEST------------------------
# Change the criteria based on desired output...
alpha = 0.0000001  # Learning rate for gradient of Cost function J(theta)
ep = 0.01  # Convergence criteria
iterations = 10000  # Max number of iterations

X, y = get_data()
run_test(alpha, X, y, ep, iterations)
