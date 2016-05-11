# MIT 6.189
# Exam Problem 2
# Author: Hao Zhang
# Date: 2016.4.30
# File: ex2.py

def eval_poly(x, coeff_list):
    n = len(coeff_list)
    rlt = 0
    for i in xrange(n):
        rlt += coeff_list[n - 1 - i] * x**i
    return rlt

def test():
    print eval_poly(1, [])
    print eval_poly(1, [0, 0])
    print eval_poly(2, [1, 1])
    print eval_poly(2, [1, 2, 3])
    print eval_poly(2, [1, 2, 3, 4])

test()
