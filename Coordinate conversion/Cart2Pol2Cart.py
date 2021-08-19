import numpy as np

a = 1 + 1j
b = 90

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def polar_rotation(b, phi):
    radian = np.radians(b)
    phi2 = phi + radian
    return(phi2)

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)



rho,phi = cart2pol(a.real, a.imag)
p2 = polar_rotation(b,phi)
x,y = pol2cart(rho, p2)
