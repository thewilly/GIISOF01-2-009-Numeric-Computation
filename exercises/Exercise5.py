#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 19:24:18 2018

@author: willy
"""

import numpy as np

a = 1.
b = 10.**8
c = 1.

x2 = ( -2 * c ) / ( np.sqrt( ( b**2 ) - ( 4 * a * c ) ) + b )
print(x2)

residual2 = a*x2**2 + b*x2 + c
print(residual2)