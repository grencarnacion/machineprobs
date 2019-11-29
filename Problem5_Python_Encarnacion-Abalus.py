# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 08:35:24 2019

@author: ENCARNACION & ABALUS
"""

import math
import matplotlib.pyplot as plt


def x(n):
    return math.sin ((3*math.pi*n)/100)
'''not sure if x(n) is user input or provided already..'''

def y(n):
    if n == 0:
        return -1.5*x(n) + 2*x(n+1) - 0.5*x(n+2)
    elif n>0 and n <=198:
        return 0.5*x(n+1) - 0.5*x(n-1)
    elif n == 199:
        return 1.5 *x(n) - 2*x(n-1) + 0.5*x(n-2)
    
n0 = list(range(200))
x0 = [x(n) for n in n0]
y0 = [y(n) for n in n0]
    
plt.plot (n0, x0, label = 'x(n)')
plt.plot (n0, y0, label = 'y(n)')
plt.legend
plt.show
    
