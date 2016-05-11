# MIT 6.189
# Homework1 Ex 2.6 The game of Nims/Stones
# Name: Hao Zhang
# Date: 2016.4.29
# Section:
# File: nims.py

def play_nims(pile, max_stones):
    '''
    An interactive two-person game; also known as Stones.

    Two players sit in front of a pile of @pile stones. 
    They take turns, each removing between 1 and @max_stones stones (assuming there are at least @max_stones stones left in the pile).
    The person who removes the last stone(s) wins.

    @param pile: the number of stones in the pile to start
    @param max_stones: the maximum number of stones you can take on one turn
    '''
    if pile <= max_stones or max_stones < 1 or type(pile) != int or type(max_stones) != int:
        print 'The setting of pile and max_stones is not valid.'
        return

    # Basic structure of program (feel free to alter as you please):
    print 'Game begin, there are %d stones at the beginning.' % pile
    while True:
        # Ask player 1 to remove
        n1 = input('Player 1: How many stones do you want to remove, in [1, %d]: ' % max_stones)
        while not 1 <= n1 <= max_stones:
            n1 = input('Player 1: Your input is not valid, try again: ')
        
        # Take stones away.
        pile -= n1
        print 'There are %d stones left.' % pile

        # Check if player 2 can win in the next step.
        if pile <= max_stones:
            print 'Game over, player 2 wins.'
            return

        # Ask player 2 to remove
        n2 = input('Player 2: How many stones do you want to remove, in [1, %d]: ' % max_stones)
        while not 1 <= n2 <= max_stones:
            n2 = input('Player 2: Your input is not valid, try again: ')

        # Take stones away.
        pile -= n2
        print 'There are %d stones left.' % pile

        # Check if player 1 can win in the next step.
        if pile <= max_stones:
            print 'Game over, player 1 wins.'
            return



# Test case.
play_nims(-1, 3)
play_nims(5, 0)
play_nims(5, 5)
play_nims(5, 3)
