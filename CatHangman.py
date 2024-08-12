# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


###imported libraries

import random

###functions
    
def word_list():
   word = ['siamese', 'shorthair', 'persian', 'ragdoll', 'sphynx', 'burmese', 'bombay', 'siberian', 'munchkin', 'ragamuffin', 'himalayin', 'bombay', 'ocicat', 'burmilla', 'norwegianforest']
   output = list(random.choice(word))
   return output

###void main()

print("Welcome to Jeremy's cat themed hangman!")

choice = word_list()

guess_list = ['_' for x in choice]

print(choice)   #for testing, remove later
print(guess_list)   #for testing, remove later

n = 9
i = 0
while i < 10 and i >=0:
    print("Please enter a letter to guess the word:" )
    guess = input()
    for index, item in enumerate(choice):
        if guess == item:
            guess_list[index] = guess
        else:
            print("Incorrect choice, {n} attempts remaining".format(n=n))
    print(guess_list)
    i += 1
    n -= 1