import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
from scipy.optimize import fmin

data_x = np.arange(0.0,1.1,0.1)                   # "real" data
data_y = np.exp(-data_x)


#plt.plot(data_x,data_y);plt.show()
poly = np.polyfit(data_x,data_y,2)                # Using numpy polynomial fit function

def poly_compare(x0, *x):                         # Function for comparing the "real" to model
    data_x,data_y = x[0],x[1]
    model = x0[0]+data_x*x0[1]+data_x**2*x0[2]
    return((data_y-model)**2).sum()

guess = [10.,10.,10.]                             # Guesses for model
print(fmin(poly_compare, guess, (data_x,data_y))) # Use of fmin to optimise guess values using the model
