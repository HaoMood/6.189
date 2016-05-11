# MIT 6.189
# Homework 4 Graphics Module Reference
# Author: Hao Zhang
# Date: 2016.4.30
# File: graphics_demo.py

from graphics import *

# The GraphWin class implements a window where drawing can be done.
win = GraphWin('My Circle', 100, 100)
# Various GraphicsObjects are provided that can be drawn into a GraphWin.
c = Circle(Point(50, 50), 10)
c.draw(win)
win.getMouse()
win.close()
