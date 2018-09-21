# -*- coding: utf-8 -*-
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

ax.imshow(img)

xy=[]


#table with rectangles
rects=[]


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
        x=event.x
        y=event.y
        rects.append(RectArea(x,y))
        for rect in rects:
            rect.draw(fig, ax)
        
    
    


width=0.0
height=0.0


#def on_press(self, event):
    

class RectArea:
    #because rectangle or circle were not added to figure a priori - figure and axes must be passed
    def __init__(self, xi,yi):
        self.width=20
        self.height=10
        self.x0=xi
        self.y0=yi
        self.edgecol="red"
        self.r=4
        #angle is anticlockwise
        self.angle=0.0
        #storing the background of rectangle
        self.background = None
        #storing the backgroud of circle
        self.backgroundc=None
        #indicator of the selection of the rectangle - creating an instance makes it selected
        self.is_Recselected=True
        #indicator of the selection of circle
        self.is_Circselected=False
        self.rect = Rectangle((self.x0,self.y0), self.width, self.height, ec=self.edgecol, fill=False, ls="solid")
        #upper right circle - draggable
        self.xr=self.x0+self.width
        self.yr=self.y0+self.height
        self.circle=Circle((self.xr, self.yr), radius=self.r)
        #circle - origin of the rectangle -> left, bottom corner of the rectangle 
        self.circle_o=Circle((self.x0, self.y0), radius=self.r)
        self.rect.set_animated(True)
        self.circle.set_animated(True)
        
    
        
    def draw(self, fig, axes):
        canvas=fig.canvas
        canvas.draw()
        self.background=canvas.copy_from_bbox(axes.bbox)
        axes.draw_artist(self.rect)
        axes.draw_artist(self.circle)
        axes.draw_artist(self.circle_o)
        canvas.blit(axes.bbox)
        
'''     
     
    def clickRect(self):
        #clicking rectangle makes it selected
        canvas=self.rect.figure.canvas
        axes=self.rect.axes
        self.rect.set_animated(True)
        #clicking the circle makes it draggable
        
     
    def dragRect(self, x_mouse, y_mouse):
        w=x_mouse-self.x0
        h=y_mouse-self.y0
        self.rect.set_width(w)
        self.rect.set_height(h)
        #drawing of the rectangle with blit technique 
        canvas=self.rect.figure.canvas
        axes=self.rect.axes
        
        canvas.draw()
        canvas.restore_region()
    
    def releaseRect(self):
        pass
        
    def connect(self):
        'connect to all the events we need'
        self.cidpress = self.rect.figure.canvas.mpl_connect(
            'button_press_event', self.clickRect)
        self.cidrelease = self.rect.figure.canvas.mpl_connect(
            'button_release_event', self.releaseRect)
        self.cidmotion = self.rect.figure.canvas.mpl_connect(
            'motion_notify_event', self.dragRect)
   
   #disconnection
    def disconnect(self):
        'disconnect all the stored connection ids'
        self.rect.figure.canvas.mpl_disconnect(self.cidpress)
        self.rect.figure.canvas.mpl_disconnect(self.cidrelease)
        self.rect.figure.canvas.mpl_disconnect(self.cidmotion)
       
           
        
'''
    




cidpress = fig.canvas.mpl_connect('button_press_event', onclick)
  
