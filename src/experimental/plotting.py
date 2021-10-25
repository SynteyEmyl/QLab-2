"""plotting.py:
In this file we prove the graphic generated
using matplotlib.
"""

import model.hydrogen as hy
import model.numerical_methods as methods

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

SAMPLES = 7_000

fig = plt.figure()
points = fig.add_subplot(111, projection='3d')
points.set_title('\nMonte Carlo Integral of |\u03A8|^2\nin three dimensions', fontsize=18)

integral, r, theta, phi, v, psi_i = methods.spherical_monte_carlo_integral(hy.squared_h2s, samples=SAMPLES)

x_ = r * np.sin(theta) * np.cos(phi)
y_ = r * np.sin(theta) * np.sin(phi)
z_ = r * np.cos(theta)

points.scatter(x_, y_, z_, c=psi_i, norm=colors.Normalize(), alpha=0.1)
plt.show()
