# MIT 6.189
# Homework1 Ex1.8 For & While Loops
# Author: Hao Zhang
# Date: 2016.4.28
# File: loops.py

# Boolean var. to indicate whether we are at the debug state.
bool_debug = True

print '******** PART 1 ********'

for i in xrange(2, 11):
    if bool_debug:
        print i
    print 1.0 / i


print '******** PART 2 ********'

n = input('Please input a pos. int: ')
if type(n) != int or n < 0:
    print 'This input number is illegal.'
else:
    for i in xrange(n, -1, -1):
        print i


print '******** PART 3 ********'

base = input('Please input a base: ')
exp = input('Please input a exp: ')
rlt = 1
for i in xrange(abs(exp)):
    rlt *= base
if exp < 0:
    rlt = 1.0 / rlt
print 'base ** exp is', rlt


print '******** PART 4 ********'

n = input('Please input a number that is divisible by 2: ')

while type(n) != int or n % 2 != 0:
    n = input('This is not the correct number, try again: ')
print 'You finally got it right!'
