# MIT 6.189
# Exam 1
# Author: Hao Zhang
# Date: 2016.4.30
# File: ex1.py

from math import sqrt

def sol_quad(a, b, c):
    '''
    Sol. f(x) = a * x**2 + b * x + c
    '''
    if a == 0:
        print 'Error: a is 0.'
    else:
        det = b**2 - 4 * a * c
        if det == 0:
            x = -b * 1.0 / (2 * a)
            return x, x
        elif det < 0:
            x1 = (-b + sqrt(-det) * 1j) * 1.0 / (2 * a)
            x2 = (-b - sqrt(-det) * 1j) * 1.0 / (2 * a)
            return x1, x2
        else:
            x1 = (-b + sqrt(det)) * 1.0 / (2 * a)
            x2 = (-b - sqrt(det)) * 1.0 / (2 * a)
            return x1, x2


def test():
    print sol_quad(0, 1, 2)
    print sol_quad(1, 2, 1)
    print sol_quad(1, 1, 1)
    print sol_quad(1, 4, 1)


test()
