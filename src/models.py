import numpy as np
from scipy.optimize import curve_fit

def exponential_decay(x, a, b): # Retention Formula derived from the case: a * e^(-b * (x-1))
    return a * np.exp(-b * (x - 1))

def fit_retention_curve(days, rates): # To deploy retention formula, use least squares method to find a and b
    params, _ = curve_fit(exponential_decay, days, rates) # Get the most viable a and b values
    return params

def get_predicted_retention(day, a, b): # Calls exponential_decay, ease of read
    return exponential_decay(day, a, b)