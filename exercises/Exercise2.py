#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 19:25:05 2018

@author: willy
"""
import numpy as np

x = 0.1
    
def de2bi_b(x):
    decimal = x - int(np.fix(x))
    l = []
    limit = 1;
    
    while decimal != 0 and limit < 24:
        decimal = decimal * 2
        if decimal >= 1.0 :
            l.append(1)
            decimal = decimal - 1.0
        else:
            l.append(0)
            
        limit = limit + 1
    return l

#print(de2bi_b(x))