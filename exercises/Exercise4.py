#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 19:02:20 2018

@author: willy
"""

import sys

i = -52;
sum = 1;

while(i < 0):
    sum += 1 * 2**i
    i = i+1
    
sum *= 2**1023

print(sum)
print(sum == sys.float_info.max)