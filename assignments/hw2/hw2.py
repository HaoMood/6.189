# MIT 6.189
# Homework2
# Name: Hao Zhang
# Date: 2016.4.29
# Section:
# File: hw2.py

##### Template for Homework 2, exercises 2.0 - 2.5  ######

# **********  Exercise 2.0 ********** 

def f1(x):
    print x + 1

def f2(x):
    return x + 1

# **********  Exercise 2.1 ********** 

# Define your function here
##### YOUR CODE HERE #####

# Test Cases for Exercise 2.1
##### YOUR CODE HERE #####

# ********** Exercise 2.2 ********** 

# Define is_divisible function here
##### YOUR CODE HERE #####
def is_divisible(m, n):
    if n == 0:
        return False
    return m % n == 0

# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function
print is_divisible(10, 5)  # This should return True
print is_divisible(18, 7)  # This should return False
print is_divisible(42, 0)  # What should this return?


# Define not_equal function here
##### YOUR CODE HERE #####
def not_equal(x, y):
    return not x == y

# Test cases for not_equal
##### YOUR CODE HERE #####
print not_equal(5, 5)
print not_equal(1, 5)
print not_equal(0, 0)

# ********** Exercise 2.3 ********** 
import math
## 1 - multadd function
##### YOUR CODE HERE #####
def multadd(a, b, c):
    return a * b + c

## 2 - Equations
##### YOUR CODE HERE #####


# Test Cases
angle_test = multadd(math.sin(math.pi / 4), 1, math.cos(math.pi / 4) / 2)
print "sin(pi/4) + cos(pi/4)/2 is:"
print angle_test

ceiling_test = multadd(math.ceil(276.0 / 19), 1, multadd(2, math.log(12, 7), 0))
print "ceiling(276/19) + 2 log_7(12) is:"
print ceiling_test

## 3 - yikes function
##### YOUR CODE HERE #####
def yikes(x):
    return multadd(x, math.exp(-x), math.sqrt(1 - math.exp(-x)))

# Test Cases
x = 5
print "yikes(5) =", yikes(x)

# ********** Exercise 2.4 **********

## 1 - rand_divis_3 function
##### YOUR CODE HERE #####
import random
def rand_divis_3():
    return random.randint(0, 100) % 3 == 0

# Test Cases
##### YOUR CODE HERE #####
print rand_divis_3()
print rand_divis_3()
print rand_divis_3()

## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has
##### YOUR CODE HERE #####
def roll_dice(sides, n):
    # sildes: the number of sides of the die
    # n: the number of dice to roll
    if sides <= 0:
        print 'Sides must > 0!'
        return 
    for i in range(n):
        print random.randint(1, sides)
    print 'That\'s all!'


# Test Cases
##### YOUR CODE HERE #####            
roll_dice(6, 3)
roll_dice(4, 0)
roll_dice(0, 4)
roll_dice(-2, 2)


# ********** Exercise 2.5 **********

# code for roots function
##### YOUR CODE HERE #####   
def roots(a, b, c):
    # Find the root of quad. f(x) = a * x**2 + b * x + c.
    if a == 0:
        # f(x) = b * x + c.
        if b == 0:
            # f(x) = c.
            if c == 0:
                # f(x) = 0.
                print 'It has root everywhere.'
                return None
            if c != 0:
                # f(x) = c.
                print 'It has root nowhere.'
                return None
        else:
            print 'It has one root.'
            return -1.0 * c / b
    else:
        # f(x) = a * x**2 + b * x + c.
        det = b**2 - 4 * a * c
        if det < 0:
            print 'It has complex roots.'
            x1 = 1.0 * (-b + math.sqrt(-det) * 1j) / 2 / a
            x2 = 1.0 * (-b - math.sqrt(-det) * 1j) / 2 / a
            return x1, x2
        elif det == 0:
            print 'It has double roots.'
            x = 1.0 * (-b) / 2 / a
            return x, x
        else:
            print 'It has real roots.'
            x1 = 1.0 * (-b + math.sqrt(det)) / 2 / a
            x2 = 1.0 * (-b - math.sqrt(det)) / 2 / a
            return x1, x2

# Test Cases
##### YOUR CODE HERE #####   
print roots(0, 0, 0)
print roots(0, 0, 1)
print roots(0, 1, 0)
print roots(1, 1, 1)
print roots(1, -2, 1)
print roots(1, 3, 1)


