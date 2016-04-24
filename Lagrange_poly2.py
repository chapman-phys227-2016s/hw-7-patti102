#! /usr/bin/env python

"""
File: read_2columns.py

Copyright (c) 2016 Taylor Patti

License: MIT

This module provides a graphing function which serves the
module Lagrange_poly1. The former is imported automatically
in the opening statements of this module.

"""

import numpy as np
import math
from matplotlib.pylab import *

import Lagrange_poly1 as p1

def graph(f, n, xmin, xmax, resolution=1001):
    """Creates a graph of a given function f by both plotting n evenly spaced
    points of the function on the given interval as black circles, and by plotting
    a blue line of the given resolution by the interpolating function p_L and its
    property L_k of the module Lagrange_poly1"""
    x_actual = np.linspace(xmin, xmax, n)
    y_actual = f(x_actual)
    x_array = np.linspace(xmin, xmax, resolution)
    y_array = np.array([p1.p_L(x, x_actual, y_actual) for x in x_array])
    plot(x_actual, y_actual, 'ko')
    plot(x_array, y_array, 'b-')
    xlim([-0.01, math.pi + 0.01])
    ylim([0, 1.1])
    title('Sin and Interpolating Function from 0 to Pi')
    xlabel('x')
    ylabel('y')
    
def graph2(f, n, xmin, xmax, legend_list, resolution=1001):
    for element in n:
        x_actual = np.linspace(xmin, xmax, element)
        y_actual = f(x_actual)
        x_array = np.linspace(xmin, xmax, resolution)
        y_array = np.array([p1.p_L(x, x_actual, y_actual) for x in x_array])
        plot(x_actual, y_actual, 'o')
        plot(x_array, y_array, '-')
    legend(legend_list, loc=9)
    title('Sin and Interpolating Functions from 0 to Pi')
    xlabel('x')
    ylabel('y')
