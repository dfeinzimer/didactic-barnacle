#Version 11.10.18.2
#Adapted from http://wang.ecs.fullerton.edu/cpsc485/editdist.html
# David Feinzimer 4168
#Requirements
#   Python 3.x
#Instructions
#   In project directory run python3 main.py

from array import *

edit_distance = None
aligned_word_one = None
aligned_word_two = None
word_one = None
word_two = None

print("Welcome to Edit Distance Calculator")
print("This program calculates the edit distance between two words using dynamic programming.")
print("The lengths of the words should be less than 30 characters.")
print("Please input two words for the edit distance.")

word_one = input("The first word: ")
word_two = input("The second word: ")

print("You entered: " + word_one + " and " + word_two)
