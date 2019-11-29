# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 12:19:48 2019

@author: ENCARNACION & ABALUS
"""

# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

def f(n):
    if n < 9:
        return n*n-7
    return f(n-10)

if __name__ == '__main__':
    x = []
    y = []
    '''range'''
    for i in range (0,100):
        x.append(i)
        y.append(f(i))
        
    print (x)
    print (y)
    '''stem()'''
    plt.stem(x,y)
    '''labels'''
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Graph f(n)')