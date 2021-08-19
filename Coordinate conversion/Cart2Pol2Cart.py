import numpy as np

a = 1 + 1j
b = 90

def cart2pol(x, y): # Basic function for converting cartestian coordinates to polar
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi) 

def polar_rotation(b, phi): # Applies a rotation to the polar coordinates of 90 degrees
    radian = np.radians(b)
    phi2 = phi + radian
    return(phi2)

def pol2cart(rho, phi): # Converts back to cartesian
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)



rho,phi = cart2pol(a.real, a.imag) # .real and .imag separates the real and imaginary components of variable "a" which allows us to get an X and Y from a single variable
p2 = polar_rotation(b,phi)
x,y = pol2cart(rho, p2)
