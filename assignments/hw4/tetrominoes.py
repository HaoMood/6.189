# MIT 6.189
# Homework 4 Ex 4.3 Tetrominoes
# Author: Hao Zhang
# Date: 2016.4.30
# File: tetrominoes.py

from graphics import *

class Block(Rectangle):
    '''
    The tetris board is typically 10x20 squares, 
    where a square has a width of 30 pixels.
    Each block occupies a single square at a time.
    The position (0,0) is the top left corner of the board, 
    and (9, 19) is the bottom right corner.
    '''
    def __init__(self, pos, color):
        x = pos.getX()
        y = pos.getY()
        Rectangle.__init__(self, Point(x * 30, y * 30), Point(x * 30 + 29, y * 30 + 29))
        self.setFill(color)

class Shape:
    def __init__(self, pos_list, color):
        self.block_list = []
        for pos in pos_list:
            self.block_list.append(Block(pos, color))

    def draw(self, win):
        for block in self.block_list:
            block.draw(win)

class I_Shape(Shape):
    def __init__(self, center):
        x = center.x
        y = center.y
        coords = [Point(x - 2, y), Point(x - 1, y), Point(x, y), Point(x + 1, y)]
        Shape.__init__(self, coords, 'blue')

class J_Shape(Shape):
    def __init__(self, center):
        x = center.x
        y = center.y
        coords = [Point(x - 1, y), Point(x, y), Point(x + 1, y), Point(x + 1, y + 1)]
        Shape.__init__(self, coords, 'pink')

class L_Shape(Shape):
    def __init__(self, center):
        x = center.x
        y = center.y
        coords = [Point(x - 1, y + 1), Point(x - 1, y), Point(x, y), Point(x + 1, y)]
        Shape.__init__(self, coords, 'sky blue')

class O_Shape(Shape):
    def __init__(self, center):
        x = center.x
        y = center.y
        coords = [Point(x - 1, y), Point(x - 1, y + 1), Point(x, y), Point(x, y + 1)]
        Shape.__init__(self, coords, 'red')

class S_Shape(Shape):
    def __init__(self, center):
        x = center.x
        y = center.y
        coords = [Point(x - 1, y), Point(x, y), Point(x + 1, y), Point(x + 1, y + 1)]
        Shape.__init__(self, coords, 'green')

class T_Shape(Shape):
    def __init__(self, center):
        x = center.x
        y = center.y
        coords = [Point(x - 1, y), Point(x, y), Point(x, y + 1), Point(x + 1, y)]
        Shape.__init__(self, coords, 'yellow')

class Z_Shape(Shape):
    def __init__(self, center):
        x = center.x
        y = center.y
        coords = [Point(x - 1, y), Point(x, y), Point(x, y + 1), Point(x + 1, y + 1)]
        Shape.__init__(self, coords, 'purple')


# Test Code.
def test_block():
    win = GraphWin('Tetrominoes', 150, 150)

    # the block is drawn at position (1, 1) on the board
    # the __init__ method for your block should deal with converting
    # the Point into pixels
    block = Block(Point(1, 1), 'red')
    block.draw(win)

    win.mainloop()

def test_I_shape():
    win = GraphWin('Tetrominoes', 200, 150)

    shape = I_Shape(Point(3, 1))
    shape.draw(win)

    win.mainloop()

def test_tetrominoes():
    win = GraphWin('Tetrominoes', 900, 150)

    # a list of shape classes
    tetrominoes = [I_Shape, J_Shape, L_Shape, O_Shape, S_Shape, T_Shape, Z_Shape]
    x = 3
    for tetromino in tetrominoes:
        shape = tetromino(Point(x, 1))
        shape.draw(win)
        x += 4
    
    win.mainloop()

# test_block()
# test_I_shape()
test_tetrominoes()
