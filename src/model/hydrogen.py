"""hydrogen.py:
this file contains the implementation of the 
real valued hydrogen wave functions.
"""

__author__ = 'Miguel Angel Avila Torres'
__copyright__ = 'Copyright 2021, hydro-wave-visualizer'
__credits__ = ['Miguel Angel Avila Torres']
__license__ = 'The Legacy License'
__version__ = '1.0.0'
__maintainer__ = f'{__author__}'
__email__ = None
__status__ = 'Release'


import numpy as np

a_0: float = 5.29177210903E-11  # First Bohr Radius


def hydrogen_1s(r: float, theta: float = 0, phi: float = 0):
    return np.exp(-r/a_0) / (np.sqrt(np.pi)*a_0**(3/2))


def hydrogen_2s(r: float, theta: float = 0, phi: float = 0):
    return (2 - (r / a_0)) * np.exp(-r/(2*a_0)) / (4*np.sqrt(2*np.pi)*a_0**(3 / 2))


def hydrogen_2p(r: float, theta: float = 0, phi: float = 0):
    return ((r/a_0)*np.exp(-r/(2*a_0))*np.cos(theta)) / (4*np.sqrt(2*np.pi)*a_0**(3 / 2))


def hydrogen_3s(r: float, theta: float = 0, phi: float = 0):
    return (27 - 18*(r/a_0) + 2*((r**2)/(a_0**2))) * (np.exp(-r/(3*a_0))) / (81*np.sqrt(3*np.pi)*a_0**(3/2))


def hydrogen_3p(r: float, theta: float = 0, phi: float = 0):
    return np.sqrt(2) * (6 - (r/a_0)) * (r/a_0) * np.exp(-r/(3*a_0)) * np.cos(theta) / (81*np.sqrt(np.pi)*a_0**(3/2))


def hydrogen_3d(r: float, theta: float = 0, phi: float = 0):
    return ((r**2)/(a_0**2)) * np.exp(-r/(3*a_0)) * (3*(np.cos(theta)**2) - 1) / (81*np.sqrt(6*np.pi)*a_0**(3/2))


def squared_h1s(r: float, theta: float, phi: float):
    return hydrogen_1s(r, theta, phi) ** 2


def squared_h2s(r: float, theta: float, phi: float):
    return hydrogen_2s(r, theta, phi) ** 2


def squared_h2p(r: float, theta: float, phi: float):
    return hydrogen_2p(r, theta, phi) ** 2


def squared_h3s(r: float, theta: float, phi: float):
    return hydrogen_3s(r, theta, phi) ** 2


def squared_h3p(r: float, theta: float, phi: float):
    return hydrogen_3p(r, theta, phi) ** 2


def squared_h3d(r: float, theta: float, phi: float):
    return hydrogen_3d(r, theta, phi) ** 2


