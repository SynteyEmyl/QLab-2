"""mainframe.py:
This file contains the setup for the tkinter graphical
interface. On it are defined the date captors and the frames
to display the data fields, inputs and the resulting plots.
"""

__author__ = 'Miguel Angel Avila Torres'
__copyright__ = 'Copyright 2021'
__credits__ = ['Miguel Angel Avila Torres']
__license__ = 'The Legacy License'
__version__ = '1.0.0'
__maintainer__ = f'{__author__}'
__email__ = None
__status__ = 'Release'


from tkinter import *

import view.MonteCarloProbabilityGraph as MonteCarlo
import model.numerical_methods as methods
import model.hydrogen as hy

import numpy as np


app = Tk()
main_frame = Frame()


"""
Assembly section for spatial parameters in the wave functions
"""


def fill_data_captors(arguments: dict, default_values: list, plotter: Frame):
    """
    Fills the data captors (Entries) that will be passed to
    the plotter so that this can request input data to update the graphs
    :param arguments: the arguments for the plotter
    :param default_values: the arguments default values
    :param plotter: the Frame which will plot a required numerical method
    """
    y = 0
    for arg in arguments.keys():
        arguments[arg] = StringVar(app)
        Label(master=plotter, text=arg, padx=10, pady=5).grid(row=y, column=0)
        Entry(master=plotter, width=20, textvariable=arguments[arg]).grid(row=y, column=1)
        arguments[arg].set(default_values[y])
        y += 1


monte_carlo_plotter = Frame(master=app, relief='raised', borderwidth=5)

spatial_integral_arguments = {'r_a': None, 'r_b': None,
                              '\u03B8_a': None, '\u03B8_b': None,
                              '\u03D5_a': None, '\u03D5_b': None,
                              'Samples': None}
spatial_integral_values = [0, 6.73E-11, 0, np.pi * 2, 0, np.pi, methods.MONTE_CARLO_SAMPLING]

fill_data_captors(spatial_integral_arguments, spatial_integral_values, monte_carlo_plotter)

"""
Assemble section for eigenfunction chooser
"""

eigenfunction = StringVar()
eigenfunction.set('\u03A8 1s')


def fill_radio_buttons(args: dict, btn_group: Frame):
    y = 0
    for k in args.keys():
        Radiobutton(master=btn_group, text=k,
                    variable=eigenfunction, value=k).grid(row=y, column=0)
        y += 1


eigenfunction_chooser = Frame(master=app, relief='raised', borderwidth=5)

eigenfunctions_dict = {'\u03A8 1s': hy.squared_h1s, '\u03A8 2s': hy.squared_h2s,
                       '\u03A8 2p': hy.squared_h2p, '\u03A8 3s': hy.squared_h3s,
                       '\u03A8 3p': hy.squared_h3p, '\u03A8 3d': hy.squared_h3d}

fill_radio_buttons(eigenfunctions_dict, eigenfunction_chooser)

"""
Assemble section for
"""
monte_carlo_graph = Frame(master=app, width=750, height=470, relief='raised', borderwidth=5)

monte_carlo_plotter.grid(row=1, column=1)
eigenfunction_chooser.grid(row=1, column=2)
monte_carlo_graph.grid(row=1, column=3)

MonteCarlo.MonteCarloProbabilityGraph(monte_carlo_graph, spatial_integral_arguments,
                                      eigenfunction, eigenfunctions_dict)

app.mainloop()
