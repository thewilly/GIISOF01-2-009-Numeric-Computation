#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 19:37:50 2018

@author: willy
"""

import numpy as np

a = 1.
b = -10.**8
c = 1

x3 = (- b - np.sqrt(b**2 - 4*a*c)) / (2*a)
print(x3)

x4 = ((- b - np.sqrt(b**2 - 4*a*c)) / (2*a))**2

residual4 = a*x4**2 + b*x4 + c
print(residual4)