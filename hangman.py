#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 19:56:01 2023

@author: jeremy
"""

###modules
import random as rand

###functions

def choose_word():
    print("You will be assigned a random word")
    choices = ["calico", "russianblue", "tortie", "mainecoon", "sphynx", "siamese", "ragamuffin", "ragdoll", "shorthair", "persian", "burmese", "siamese", "chartreux", "pallas", "snowshoe" ]
    word = choices[rand.randrange(0, len(choices))]
    return word


def guess_word(word, guess_array, turns):
    print("You have {n} turns remaining".format(n=turns))
    global a #remove later
    a = 5    #remove later
    guess = input("Please enter your guess:" )
    
    if len(guess) == 1:
        for i in range(0, len(word)):
            if word[i] == guess:
                guess_array[i] = guess
        if guess not in word:
            turns -= 1
        print(guess_array)
    else:
        if word == guess:
            print("Correct! You have earned a muffin!")
            return guess_array
        else:
            turns -= 1
    
    if word == "".join(guess_array):
        print("Correct! You have earned a muffin!")
        return guess_array
    elif turns == 0:
        print("You have no turns remaining")
        print("Your word was {w}".format(w=word))
        return 0
    guess_word(word, guess_array, turns)
    
    
###main

print("Welcome to Jeremy's cat themed hangman game!")

word = choose_word()
guess_array = []
for i in word:
    guess_array.append("_")
    
turns = 10

#print(word)           #remove after testing
#print(guess_array)    #remove after testing
#print("".join(guess_array))    #remove after testing

guess_word(word, guess_array, turns)

#future fixes:
#   allow for uppercase letter guesses. turn guess to lower case automatically once entered
#   if answer entered already, produce error message and continue
#   -can be done by entering guesses into another array. Scan array for that letter. if in array, return error