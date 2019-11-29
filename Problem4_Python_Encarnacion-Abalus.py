# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 08:16:10 2019

@author: ENCARNACION & ABALUS
"""
import math
import matplotlib.pyplot as plt


def projectile(h, v, angle, accx, accy):
        if accy==0:
            print ("Error")
            return
        
        xval = []
        yval = []
        ''' angle '''
        vx = v*math.cos(angle*(3.141/180))
        vy = v*math.sin(angle*(3.141/180))
        
        t = 0
        x = 0
        y = h
        d = 0.0001
        
        xval.append(x)
        yval.append(y)
        
        while(True):
            t = t+d
            
            x = vx*t +(0.5)*accx*(t*t)
            y = vy*t +(0.5)*accy*(t*t) + h
            
            xval.append(x)
            yval.append(y)
            
            if y < d:
                break
        '''plots'''    
        plt.plot(xval, yval)
        ax = plt.gca()
        ax.set_ylim([0, max(yval)])
        plt.xlabel('X Axis')
        plt.ylabel('Y Axis')
        plt.title('Projectile Motion')
        plt.grid
        plt.show
        
if __name__ == '__main__':
    h = 2
    v = 5
    angle = 45
    accx = 0
    accy = -9.81
        
    projectile(h, v, angle, accx, accy)
        
        
        