# MIT 6.189
# Homework1 Ex1.7 Rock, Paper, Scissors
# Author: Hao Zhang
# Date: 2016.4.27
# File: rps.py

# Boolean var. to indicate whether or not we are in debug state.
bool_debug = False

# Convert string to corresponding integer.
#   paper -> 0
#   rock -> 1
#   scissors -> 2
def str2int(str_in):
    if str_in == 'paper':
        int_in = 0
    elif str_in == 'rock':
        int_in = 1
    elif str_in == 'scissors':
        int_in = 2
    else:
        return
    return int_in

# Get string input and convert to integer.
str_in1 = raw_input('Player 1? ')
str_in2 = raw_input('Player 2? ')

int_in1 = str2int(str_in1)
int_in2 = str2int(str_in2)

# Check for result.
if int_in1 == None or int_in2 == None:
    print 'This is not a valid object selection'
else:
    if bool_debug:
        print 'int_in1 =', int_in1, ', int_in2 =', int_in2

    # Show result.
    if int_in1 == int_in2:
        print 'There is a tie.'
    elif (int_in1 + 1) % 3 == int_in2:
        print 'Player 1 wins.'
    else:
        print 'Player 2 wins.'
