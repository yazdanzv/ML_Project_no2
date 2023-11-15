import numpy as np

def cost_function( x, y, theta0, theta1 ):
    """Compute the squared error cost function

    Inputs:
    x        vector of length m containing x values
    y        vector of length m containing y values
    theta_0  (scalar) intercept parameter
    theta_1  (scalar) slope parameter

    Returns:
    cost     (scalar) the cost
    """
    

    ##################################################
    # TODO: write code here to compute cost correctly
    # To Do Start
    # Hypothesis function for linear regression
    h_theta = theta0 + theta1 * x

    # Square error cost function
    cost = (1 / 2) * np.sum((h_theta - y)**2)
    # To Do End

    return cost
    ##################################################


def gradient(x, y, theta_0, theta_1):
    """Compute the partial derivative of the squared error cost function

    Inputs:
    x          vector of length m containing x values
    y          vector of length m containing y values
    theta_0    (scalar) intercept parameter
    theta_1    (scalar) slope parameter

    Returns:
    d_theta_0  (scalar) Partial derivative of cost function wrt theta_0
    d_theta_1  (scalar) Partial derivative of cost function wrt theta_1
    """
    
    ##################################################
    # TODO: write code here to compute partial derivatives correctly
    # To Do Start
    m = len(y)  # Number of training examples

    # Hypothesis function for linear regression
    h_theta = theta_0 + theta_1 * x

    # Partial derivatives of the cost function
    d_theta_0 = np.sum(h_theta - y)
    d_theta_1 = np.sum((h_theta - y) * x)
    # To Do End
    ##################################################

    return d_theta_0, d_theta_1 # return is a tuple

def explicit_answer(x, y):
    """Compute the explicit values of theta1 and theta2

    Inputs:
    x          vector of length m containing x values
    y          vector of length m containing y values

    Returns:
    theta_0  (scalar) intercept of line
    theta_1  (scalar) slope of line
    """
    
    
    ##################################################
    # TODO: write code here to compute explicit values of theta_0 and theta_1
    # To Do Start
    # Calculate means
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    # Calculate theta_1 based on formula
    numerator = np.sum((x - mean_x) * (y - mean_y))
    denominator = np.sum((x - mean_x)**2)
    theta_1 = numerator / denominator

    # Calculate theta_0 based on formula
    theta_0 = mean_y - theta_1 * mean_x
    return theta_0, theta_1
    # To Do End
    ##################################################