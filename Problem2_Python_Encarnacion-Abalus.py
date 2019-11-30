# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 07:20:23 2019

@author: ENCARNACION & ABALUS
"""

'''still need some debugging, giving wrong answers'''
from math import sqrt
from math import pow

def Circ (ax, ay, bx, by, cx, cy):
    
    '''x and y '''
    x1 = ax - bx
    x2 = ax - cx
    
    y1 = ay - by
    y2 = ay - cy
       
    
    x3 = cx -ax
    x4 = bx - ax
    
    y3 = cy -ay
    y4 = by - ay
    
    
    '''pow() '''
    
    xac = pow (ax,2) - pow(cx,2)
    
    yac = pow (ay,2) -pow (cy,2)
    
    xba = pow (bx, 2) - pow (ax,2)
    
    yba = pow(by,2) - pow(ay,2)
    
    ''' equations '''
    
    f = (((xac)*(x1) + (yac)*(x1) + (xba)*(x2) + (yba)*(x2) / (2* ((y3)* (x1) - (y4) * (x2)))))
      
    g = (((xac)*(y1) + (yac)*(y1) + (xba)*(y2) + (yba)*(y2) / (2* ((x3)* (y1) - (x4) * (y2)))))
       
    c = (-pow(ax,2) - pow (ay,2) - 2 * g * ax -2 * f * ay)
    
    h = -f
    k = -g
    
    sqrr = h*h + k*k -c
    r = round (sqrt(sqrr), 5)
    l = [2*g, 2*f, c]
    
    print("Center = (", h, " , ", k, ")")
    print ("Radius =", r)   
    print ("Vector [D,E,F]", l)
    
    '''plot'''
    print ('NOTE: Separate Coordinates with Space')    
    ax,ay = map (int, input ('enter first coordinates: ').split())
    bx,by = map (int, input ('enter second coordinates: ').split())
    cx,cy = map (int, input ('enter third coordinates: ').split())
    
    Circ (ax, ay, bx, by, cx, cy)

    
    
    
    
    
