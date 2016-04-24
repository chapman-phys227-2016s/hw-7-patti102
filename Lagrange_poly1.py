#! /usr/bin/env python

"""
File: read_2columns.py

Copyright (c) 2016 Taylor Patti

License: MIT

This module constructs the necesarry functions for the Lagrange Interpolation Formula
and allows the user to implement them to find the values inbetween given data points
by constructing polynomials of the same order.

"""

import numpy as np
import math

def L_k(x, k, xp, yp):
    xk = xp[k]
    xp = np.delete(xp, k) #note that it is now one shorter
    mash = np.array([((x - i) / float(xk - i)) for i in xp])
    return np.prod(mash)

def p_L(x, xp, yp):
    addem = np.array([yp[i] * L_k(x, i, xp, yp) for i in range(len(xp))])
    return np.sum(addem)

def test_p_L():
    xp = np.linspace(0, math.pi, 5)
    print xp
    yp = np.sin(xp)
    print yp
    sum = 0
    for i in xrange(len(xp)):
        sum = sum + abs(p_L(xp[i], xp, yp) - yp[i])
    apt = sum < 1e-3
    msg = 'Sum is too large for accurate information.'
    assert apt, msg

