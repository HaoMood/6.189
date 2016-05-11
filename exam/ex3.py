# MIT 6.189
# Exam Problem 3
# Author: Hao Zhang
# Date: 2016.4.30
# File: ex3.py

def make_change(cost, paid):
    '''
    A clerk has an unbounded number of bills in each of the following
    denominations: $1, $2, $5, $10, and $20.
    This function prints how to make change using the smallest 
    possible number of bills.
    '''
    if paid < cost:
        print 'Oh, you have not paid enough money!'
        return
    if paid == cost:
        print 'Great, your payment is just right!'
        return

    change = paid - cost    # Amount need to be change.
    for money in [20, 10, 5, 2, 1]:
        n = 0
        while money * n <= change:
            n += 1
        n -= 1  # Count how many to change.
        change -= money * n # Pay the customer that amount of change.

        if n != 0:
            print 'Change to you %d * $%d.' % (n, money)

def test():
    make_change(20, 15)
    make_change(20, 20)
    make_change(20, 50)
    make_change(20, 40)
    make_change(20, 88)

test()
