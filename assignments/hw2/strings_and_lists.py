# MIT 6.189
# Homework1
# Name: Hao Zhang
# Date: 2016.4.29
# Section:
# File: strings_and_lists.py

# **********  Exercise 2.7 **********

def sum_all(number_list):
    # number_list is a list of numbers
    total = 0
    for num in number_list:
        total += num

    return total

# Test cases
print "sum_all of [4, 3, 6] is:", sum_all([4, 3, 6])
print "sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4])


def cumulative_sum(number_list):
    # number_list is a list of numbers

    ##### YOUR CODE HERE #####
    A = number_list[:]  # Copy the list.
    for i in xrange(1, len(A)):
        A[i] += A[i - 1]
    return A


# Test Cases
##### YOUR CODE HERE #####
print "cumulative_sum of [4, 3, 6] is:", cumulative_sum([4, 3, 6])
print "cumulative_sum of [1, 2, 3, 4] is:", cumulative_sum([1, 2, 3, 4])
print cumulative_sum([])
print cumulative_sum([1])

# **********  Exercise 2.8 **********

def report_card():
    ##### YOUR CODE HERE #####
    # Get input.
    n = input('How many classes did you take? ')
    if n <= 0:
        print 'REPORT CARD:'
        print 'You have not take any course yet.'
        return
    classes = []
    grades = []
    for i in xrange(n):
        class_i = raw_input('What was the name of this class? ') 
        grade_i = input('What was your grade? ')
        classes.append(class_i)
        grades.append(grade_i)

    # Print out.
    print 'REPORT CARD:'
    for i in xrange(n):
        print classes[i], '\t', grades[i]
    print 'Overall GPA', sum(grades) * 1.0 / n

# Test Cases
## In comments, show the output of one run of your function.
report_card()

# **********  Exercise 2.9 **********

# Write any helper functions you need here.

VOWELS = ['a', 'e', 'i', 'o', 'u']

def pig_latin(word):
    # word is a string to convert to pig-latin
    # Pig Latin takes the first letter of a word, puts it at the end,
    # and appends 'ay'. 
    # The only exception is if the first letter is a vowel,
    # in which case we keep it as it is and append 'hay' to the end.

    if len(word) == 0:
        return word

    if len(word) == 1 and word[0] not in VOWELS:
        return word + 'ay'

    ##### YOUR CODE HERE #####
    if word[0] in VOWELS:
        return word + 'hay'
    else:
        return word[1:] + word[0] + 'ay'

# Test Cases
##### YOUR CODE HERE #####
print pig_latin('boot')
print pig_latin('image')
print pig_latin('')
print pig_latin('i')
print pig_latin('k')

# **********  Exercise 2.10 **********
# Test Cases
##### YOUR CODE HERE #####
print [i**3 for i in xrange(1, 11)]
print [i + j for i in 'ht' for j in 'ht']
s = raw_input('Please input a string: ')
print [i for i in s if i in 'aeiou' or i in 'AEIOU']
print [x + y for x in [10, 20, 30] for y in [1, 2, 3]]

# **********  Exercise OPT.1 **********
# If you do any work for this problem, submit it here 
