#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 18:22:46 2018

@author: willy
"""

import numpy as np

x = 3.67
y = np.fix(x);
print('x = ', x, 'y = ', y)
#%% First Exmaple
a = 3
b = 2
if a == 3:
    print('hello')
elif b == 2:
    print('bye')
else:
    print('none')
#%% List example
l = []
for i in range(5):
    l.append(i)
l.reverse()
print(l)
#%% Another list example
na = np.zeros(5)
for i in range(5):
    na[i] = i
    na = na[::-1]
print(na)
#%% Range and Arange exmaples
c = range(5, 10)
d = np.arange(5, 10)
e = c[:-1]
f = d[:-1]
#%% while loops example
k = 0
while k<7:
    k += 1
    print(k)
#%% functions
def square(x):
    sq = x*x
    return sq
#----------------
x = 4.56
print(square(x))







