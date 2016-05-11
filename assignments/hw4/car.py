# MIT 6.189
# Homework 4 Ex 4.2 Drawing A Car
# Author: Hao Zhang
# Date: 2016.4.30
# File: car.py

from graphics import *
from wheel import *

class Car:
    '''
    The car will contain 3 attributes: 
    two Wheel objects and one Rectangle object (the body of the car) 
    that is horizontal and whose bottom corners correspond to 
    the centers of the wheels.
    '''
    def __init__(self, left_center, left_r, right_center, right_r, height):
        self.left_wheel = Wheel(left_center, 0.6 * left_r, left_r)
        self.right_wheel = Wheel(right_center, 0.6 * right_r, right_r)
        self.rect = Rectangle(Point(left_center.getX(), left_center.getY() - height), Point(right_center.getX(), right_center.getY()))

    def draw(self, win):
        self.rect.draw(win)
        self.left_wheel.draw(win)
        self.right_wheel.draw(win)

    def set_color(self, tire_color, wheel_color, body_color):
        self.rect.setFill(body_color)
        self.left_wheel.set_color(wheel_color, tire_color)
        self.right_wheel.set_color(wheel_color, tire_color)

    def move(self, dx, dy):
        self.rect.move(dx, dy)
        self.left_wheel.move(dx, dy)
        self.right_wheel.move(dx, dy)

    def animate(self, win, dx, dy, n):
        if n > 0:
            self.move(dx, dy)
            win.after(100, self.animate, win, dx, dy, n - 1)

def test():
    win = GraphWin('A Car', 700, 300)

    # create a car object
    # 1st wheel centered at 50,50 with radius 15
    # 2nd wheel centered at 100,50 with radius 15
    # rectangle with a height of 40
    car = Car(Point(50, 50), 15, Point(100,50), 15, 40)
    car.draw(win)

    # color the wheels grey with black tires, and the body pink
    car.set_color('black', 'grey', 'pink')
    
    # make the car move on the screen
    car.animate(win, 1, 0, 400)

    win.mainloop()

test()
