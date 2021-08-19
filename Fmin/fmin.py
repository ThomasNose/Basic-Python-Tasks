import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
from scipy.optimize import fmin

A = np.loadtxt("assign3.spec")                                              # Unloading SPEC file

wave_obs,counts = A[:,0], A[:,1]                                            # Observed wavelength (in nm) and counts 
error = np.sqrt(counts)                                                     # Error

wave1,wave2 = 495.9, 500.7                                                  # Wavelength in nm at rest
ratio = wave2/wave1

def compare(x0,*x):                                                         # Function defined
    wave_obs,counts = x[0],x[1]
    model = x0[0] + x0[1]*np.exp(-(x[0]-x0[2])**2/(x0[3]**2)) + \
            (x0[1]/3)*np.exp(-(x[0]*ratio-x0[2])**2/(x0[3]**2))             # "\" continue on next line
                                                                            # Model for fmin to fit with
    return((counts - model)**2).sum()

guess = [np.sqrt(min(counts)),max(counts),wave_obs[np.argmax(counts)],10]   # Initial guesses, error, max count value, wavelength with max counts, pixel gap

Fit = fmin(compare, guess, (wave_obs,counts))                               # Values for the fmin max counts, wavelength and band gap
                                                                            # F[0], F[1], F[2], F[3] are error, max(counts), lambda c, pixels

Z1 = (Fit[2]/wave1) - 1                                                     # Redshift calculated using optimal value from fmin 495.9nm
Z2 = (Fit[2]/wave2) - 1                                                     # Redshift calculated using optimal value from fmin 500.7nm
print(str(Z1)+" 495.9nm redshift " + '\n' + str(Z2)+" 500.7nm redshift ")   # Z = (LAMBDA REST / LAMBDA OBSERVED) - 1

x = wave_obs
Fit = Fit[0] + Fit[1]*np.exp(-(x-Fit[2])**2/(Fit[3]**2)) + \
      (Fit[1]/3)*np.exp(-(x*ratio - Fit[2])**2/(Fit[3]**2))                 # "\" continue on next line
                                                                            # The modelling data fit with the optimal values from fmin

plt.plot(wave_obs,counts,label='Actual data')                               # Actual data plotted 
plt.plot(wave_obs,Fit,label='Modelled data')                                # Model data plotted

plt.ylabel("Counts")                                                        # Adding labels and legend to graph
plt.xlabel("Wavelength (nm)")
plt.title("Model fit")
plt.legend(loc='best')
plt.savefig("Plot.png")
plt.show()




