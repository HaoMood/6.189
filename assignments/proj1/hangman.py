# MIT 6.189
# Project 1 Hangman
# Name: Hao Zhang
# Date: 2016.4.29
# Section: 
# 6.189 Project 1: Hangman template
# File: hangman.py

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = split(line)
    print "  ", len(wordlist), "words loaded."
    print 'Enter play_hangman() to play a game of hangman!'
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
secret_word = 'claptrap' 
letters_guessed = []

# From part 3b:
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.

    Eg, if letters_guessed = ['a', 'l', 'm', 'c', 'e', 't', 'r', 'p', n],
    then function will return True.
    if letters_guessed = ['e', 'l', 'q', 't', 'r', 'p', 'n'],
    then function will return False.
    '''
    global secret_word
    global letters_guessed

    ####### YOUR CODE HERE ######
    for c in secret_word:
        if c not in letters_guessed:
            return False
    return True


def print_guessed():
    '''
    Prints out the characters you have guessed in the secret word so far

    It returns a string that contains the word with a dash '-' in place of letters not guessed yet
    '''
    global secret_word
    global letters_guessed
    
    ####### YOUR CODE HERE ######
    out = []
    for c in secret_word:
        if c in letters_guessed:
            out.append(c)
        else:
            out.append('-')
    return out

def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0

    # Update secret_word. Don't uncomment this line until you get to Step 8.
    secret_word  = get_word()

    ####### YOUR CODE HERE ######
    while True:
        print MAX_GUESSES - mistakes_made, 'guesses left.'
        print print_guessed()

        # Get user's input.
        c = raw_input('Please make a guess: ')
        c = c.lower()
        # Check whether it is a valid letter.
        while len(c) != 1 or c not in lowercase:
            c = raw_input('The input is not valid, please try again: ')
        # Check whether this letter has already been guessed.
        while c in letters_guessed:
            c = raw_input('This letter has already been guessed, try again: ')
        
        letters_guessed.append(c)   # Append c
        if c not in secret_word:
            mistakes_made += 1

        if mistakes_made >= MAX_GUESSES:
            print 'You lose! the secret word is', secret_word
            return 
        if word_guessed():
            print 'You win! the secret word is', secret_word
            return

# Test.
play_hangman()
