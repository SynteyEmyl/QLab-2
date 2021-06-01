# -----------------------------------------------------------------------------
# Copyright (c) 2020, Miguel Angel Avila Torres. All Rights Reserved.
# -----------------------------------------------------------------------------
import model.numerical_methods as methods

import numpy as np
import matplotlib.colors as colors

from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class MonteCarloProbabilityGraph(object):

    def __init__(self, window: Frame, integral_params: dict,
                 eigenfunction: StringVar, eigenfunctions_dict: dict, meridians: int = 20):
        """
        :param window: The frame which will draw the plot
        :param integral_params: a dictionary with {str: StringVar} entries
        :param meridians: the number of meridians enclosing the radius r_b in the integral
        :param eigenfunction: a key in the eigenfunctions_dict, it maps to a squared wave function
        :param eigenfunctions_dict: {[text rep]: [squared wave function]} dictionary
        """
        self.window = window
        self.arguments = integral_params
        self.eigenfunction = eigenfunction
        self.eigenfunctions_dict = eigenfunctions_dict
        self.meridians = meridians
        self.button = Button(master=window, text='Simulate', command=self.__plot_monte_carlo_probability)
        self.button.pack()
        self.probability = Label(master=window)
        self.probability.pack()
        self.error = Label(master=window)
        self.error.pack()
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111, projection='3d')
        self.canvas = FigureCanvasTkAgg(self.fig, master=window)
        self.axes.set_box_aspect([1, 1, 1])
        self.__plot_monte_carlo_probability()

    @staticmethod
    def wire_frame_sphere(radius: float = 1E-10, n_meridians: int = 20, n_circles_latitude: float = None):
        """
        :param radius: the radius for the sphere limiting with the meridians
        :param n_meridians: the number of meridians
        :param n_circles_latitude: the latitude of the meridians
        :return: the coordinates for the meridians
        """
        if n_circles_latitude is None:
            n_circles_latitude = max(n_meridians / 2, 4)
        u, v = np.mgrid[0:2 * np.pi:n_meridians * 1j, 0:np.pi:n_circles_latitude * 1j]
        sphere_x = radius * np.cos(u) * np.sin(v)
        sphere_y = radius * np.sin(u) * np.sin(v)
        sphere_z = radius * np.cos(v)
        return sphere_x, sphere_y, sphere_z

    def __plot_monte_carlo_probability(self):
        """
        plots the monte carlo integral of the absolute squared
        hydrogen 1s wave function
        :return: None
        """
        r_a, r_b, theta_a, theta_b, phi_a, phi_b, samples = [float(e.get()) for e in self.arguments.values()]
        psi = self.eigenfunctions_dict[self.eigenfunction.get()]

        integral, r, theta, phi, v, psi_i = methods.spherical_monte_carlo_integral(
            psi, r_a, r_b, theta_a, theta_b, phi_a, phi_b, int(samples))

        self.axes.clear()

        x_ = r * np.sin(theta) * np.cos(phi)
        y_ = r * np.sin(theta) * np.sin(phi)
        z_ = r * np.cos(theta)

        self.axes.scatter(x_, y_, z_, c=psi_i + np.max(psi_i), cmap='hot', norm=colors.Normalize())
        self.axes.plot_wireframe(*self.wire_frame_sphere(r_b, self.meridians), color='red', alpha=0)
        # it saves locally the plotted image
        # self.fig.savefig(fname=f'monte-carlo-{psi.__name__}.pdf', format='pdf', dpi=1200)
        self.probability['text'] = '\nProbability: ' + str(integral) + '\n'
        self.error['text'] = 'Error: ' + str(methods.spherical_monte_carlo_estimation_error(psi, r, theta, phi,
                                                                                            v, samples))
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()
