# MIT 6.189
# Exam Problem 4
# Author: Hao Zhang
# Date: 2016.5.5
# File: ex4.py

print ('######## PART A ########')

def find_pos(s, word):
    s_list = s.split()
    ret_list = []

    for i in xrange(len(s_list)):
        if s_list[i] == word:
            ret_list.append(i)
    return ret_list

def test_find_pos():
    print find_pos('we dont need no education we dont need no thought control no we dont', 'dont')

test_find_pos()

print ('######## PART B ########')

import string

def inverted_index(s):
    s_list = s.split()
    seen_words = []

    for i in xrange(len(s_list)):
        if s_list[i] not in seen_words:
            seen_words.append(s_list[i])

            print s_list[i] + ':',

            ret_list = find_pos(s, s_list[i])
            # Transfer each elem. from int to str.
            ret_list_str = [str(pos) for pos in ret_list]
            print string.join(ret_list_str, ', ')

def test_inverted_index():
    inverted_index('we dont need no education we dont need no thought control no we dont')

test_inverted_index()
