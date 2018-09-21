#-*- coding: utf-8 -*-
"""
Created on Mon Aug 07 12:58:45 2017
@author: Marcin
"""

import  matplotlib.pyplot as plt

import matplotlib.image as mpimg

from matplotlib.patches import Rectangle

from matplotlib.patches import Circle

import numpy as np

img=mpimg.imread('Saboya_Re_648.png')


fig= plt.figure()
ax=fig.add_subplot(111)

#loading an image
ax.imshow(img)



#store the points
xy=[]


#table with rectangles
rects=[]


class recti:
    def __init__(self, x0, y0, dx, dy, axes):
        self.x0=x0
        self.y0=y0
        self.dx=dx
        self.dy=dy
        self.line=[0,0,0,0]
        self.line[0],=axes.plot([x0,x0 + dx],[y0, y0], picker=5)
        self.line[1],=axes.plot([x0 + dx, x0 + dx], [y0, y0 + dy], picker=5)
        self.line[2],=axes.plot([x0 + dx, x0], [y0+dy, y0+dy], picker=5)
        self.line[3],=axes.plot([x0, x0], [y0+dy, y0], picker=5)
    
   




#kiedy zaznacza się dane na wykresie
def onclick(event):
    if event.button==1:
        a=4.0
        x=event.xdata-a/2.0
        y=event.ydata-a/2.0
        #   store the point
        xy.append((x,y))
        rect = Rectangle((x,y), a, a, ec='black')
        ax.add_patch(rect)
        fig.canvas.draw()
    else:
        x=event.xdata
        y=event.ydata
        recti0=recti(x,y,100.0,100.0, ax)
        rects.append(recti0)
        fig.canvas.draw()
        
        
        
def onMove(event):
    for rectii in rects:
        for i in range (4):
           print(rectii.line[i].axes)
           if event.inaxes == rectii.line[i].axes:
               rectii.line[i].set_linestyle("--")
               fig.canvas.draw()
   



        
        
    
cidpress = fig.canvas.mpl_connect('button_press_event', onclick)

fig.canvas.mpl_connect('motion_notify_event', onMove)