# -*- coding: utf-8 -*-

import numpy as np

def de2bi_a(d):

    x = np.fix(d)                      # truncate fractional part
    b = []                             # initialize output as list (to append)
    
    while x/2 > 0 :
        b.append(x%2)                  # compute remainder
        x = x//2                       # compute quotient
        
    b = np.array(b, dtype=np.int8)     
    return np.flipud(b)                # flip upside-down to get correct form


def de2bi_b(d):

    aux = np.fix(d)                      # truncate fractional part
    x = d - aux                         #fractional part
    b = []                             # initialize output as list (to append)
    
    while x*2 != 0 :
        s = x*2
        n = np.fix(s)
        b.append(n)                
        x = s - n                       
        
    b = np.array(b, dtype=np.int8)     
    return b            

def ieee754(d):
    
    b= np.array([])
    mantissa = np.array([])
    entera = de2bi_a(d)
    decimal = de2bi_b(d)
#    print(int(d)>=0)
    
    if(int(d)>=0):
        zero = np.array([0])
#        print(zero)
        b = np.append(b,zero)
    else:
        one = np.array([1])
        b= np.append(b,one)
    exponent = entera.size;
    exp2 = exponent +126;
    binexp= de2bi_a(exp2);
    np.append(b,binexp)
    mantissa = np.concatenate((entera,decimal))
    mantissa = np.delete(mantissa,0);
    b = np.array(b, dtype=np.int8)  
    b = np.concatenate((b,mantissa))    
    while(b.size < 32):
#        print(b.size)
        b= np.append(b,0)
    
 #   b = np.array(b, dtype=np.int8)     
    return b;
        
print(ieee754(-1.41))