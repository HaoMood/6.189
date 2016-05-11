# MIT 6.189
# Homework 3
# Name: Hao Zhang
# Date: 2016.4.29
# Section:
# File: hw3.py

##### Template for Homework 3, exercises 3.1 - ######

# **********  Exercise 3.1 ********** 

# Define your function here
##### YOUR CODE HERE #####
def list_intersection(list1, list2):
    ret_list = []
    for x in list1:
        if x not in ret_list and x in list2:
            ret_list.append(x)
    return ret_list

# Test Cases for Exercise 3.1
##### YOUR CODE HERE #####
print list_intersection([1, 3, 5], [5, 3, 1])
print list_intersection([1, 3, 6, 9], [10, 14, 3, 72, 9])
print list_intersection([2, 3], [3, 3, 3, 2, 10])
print list_intersection([2, 4, 6], [1, 3, 5])
print list_intersection([], [])
print list_intersection([], [1, 3])
print list_intersection([1, 3], [])
print list_intersection([3, 3, 3, 2, 10], [2, 3])

# **********  Exercise 3.2 **********

# Define your function here
def ball_collide(ball1, ball2):
    ##### YOUR CODE HERE #####
    x1, y1, r1 = ball1
    x2, y2, r2 = ball2
    return abs(x1 - x2)**2 + abs(y1 - y2)**2 <= (r1 + r2)**2

# Test Cases for Exercise 3.2
print ball_collide((0, 0, 1), (3, 3, 1)) # Should be False
print ball_collide((5, 5, 2), (2, 8, 3)) # Should be True
print ball_collide((7, 8, 2), (4, 4, 3)) # Should be True

# **********  Exercise 3.3 **********

# Define your dictionary here - populate with classes from last term
my_classes = {}

def add_class(class_num, desc):
    ##### YOUR CODE HERE #####
    my_classes[class_num] = desc

# Here, use add_class to add the classes you're taking next term
add_class('6.189', 'Introduction to Python')

def print_classes(course):
    ##### YOUR CODE HERE #####
    has_course = False
    for k in my_classes.keys():
        dot_pos = k.find('.')
        if course == k[:dot_pos]:
            print k, '-', my_classes[k]
            has_course = True
    if has_course == False:
        print 'No Course', course, 'classes taken'


# Test Cases for Exercise 3.3
##### YOUR CODE HERE #####
add_class('6.01', 'Introduction to EECS')
print_classes('6')
print_classes('10')

# **********  Exercise 3.4 **********

NAMES = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank',
                 'Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']
AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

# Define your functions here
def combine_lists(l1, l2):
    comb_dict = {}
    ##### YOUR CODE HERE #####
    for i in xrange(len(NAMES)):
        comb_dict[NAMES[i]] = AGES[i]
    return comb_dict

combined_dict = combine_lists(NAMES, AGES) # Finish this line...

def people(age):
    # Use combined_dict within this function...
    ret_list = []
    for k, v in combined_dict.items():
        if v == age:
            ret_list.append(k)
    return ret_list


# Test Cases for Exercise 3.4 (all should be True)
print 'Dan' in people(18) and 'Cathy' in people(18)
print 'Ed' in people(19) and 'Helen' in people(19) and\
       'Irene' in people(19) and 'Jack' in people(19) and 'Larry'in people(19)
print 'Alice' in people(20) and 'Frank' in people(20) and 'Gary' in people(20)
print people(21) ==   ['Bob']
print people(22) ==   ['Kelly']
print people(23) ==   []

# **********  Exercise 3.5 **********

def zellers(month, day, year):
    ##### YOUR CODE HERE #####
    # A = the month of the year, with March having the value 1, 
    #   April the value 2, ..., December the value 10, 
    #   and January and February being counted as months 11 and 12 
    #   of the preceding year (in which case,subtract 1 from C)
    # B = the day of the month (1, 2, 3, ..., 30, 31)
    # C = the year of the century (e.g. C = 89 for the year 1989)
    # D = the century (e.g. D = 19 for the year 1989)
    mon2A = {'January': 11, 'February': 12, 'March': 1, 
            'April': 2, 'May': 3, 'June': 4, 'July': 5, 
            'August': 6, 'September': 7, 'October': 8}

    A = mon2A[month]
    if 11 <= A <= 12:
        year -= 1
    B = day
    C = year % 100
    D = year / 100

    W = (13 * A - 1) / 5
    X = C / 4
    Y = D / 4
    Z = W + X + Y + B + C - 2 * D
    R = Z % 7

    R2dayofweek = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 
            3: 'Wednesday', 4: 'Thursday', 5: 'Friday',
            6: 'Saturday'}
    return R2dayofweek[R]

# Test Cases for Exercise 3.5
print zellers("March", 10, 1940) == 'Sunday' # This should be True
##### YOUR CODE HERE #####
