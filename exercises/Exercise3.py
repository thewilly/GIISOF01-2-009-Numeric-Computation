#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 19:36:38 2018

@author: willy
"""

import Exercise1
import Exercise2

def sign(x):
    if(x < 0):
        return 1
    else:
        return 0
    
number = 105.8125
bias = 127

#The sign
_sign = sign(number)

#Computations
number = abs(number)
integer = Exercise1.de2bi_a(number)
decimal = Exercise2.de2bi_b(number)

#The mantissa
mantissa = integer[:]
mantissa.pop(0)
mantissa.append(decimal)

if(len(mantissa)>23):
    mantissa = mantissa[:22]
else:
    while(len(mantissa)<23):
        mantissa.append(0)

#The exponent
exponent = len(integer)-1
exponent = exponent+bias
exponent = Exercise1.de2bi_a(exponent)[:]
if(len(exponent)>=8):
    exponent = exponent[:8]
else:
    while(len(exponent)<=7):
        exponent.insert(0,0)


print('[Sign]:', _sign, '[Exponent]:', exponent, '[Mantissa]:', mantissa)






















