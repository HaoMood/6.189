# MIT 6.189
# Project 1
# Author: Hao Zhang
# Date: 2016.4.29
# File: ex1.py

def all_less_6(A):
    for x in A:
        if x >= 6:
            return False
    return True

print all_less_6([1, 5, 3, 4])
print all_less_6([5, 3, 7, 5])

def some_less_6(A):
    for x in A:
        if x < 6:
            return True
    return False

print some_less_6([7, 8, 7, 9])
print some_less_6([7, 2, 5, 8])
