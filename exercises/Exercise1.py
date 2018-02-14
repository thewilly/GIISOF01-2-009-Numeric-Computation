#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 18:54:52 2018

@author: willy
"""
import numpy as np

def de2bi_a(x):
    p = int(np.fix(x))
    l = []

    while p > 0:
        l.append(int(np.fix(p%2)))
        p = (np.fix(p)/2)

    l = l[:-1]
    l.reverse()
    return l

x = 105.8125
binary1 = de2bi_a(x)
print(binary1)