#Version 11.10.18.3
#Adapted from http://wang.ecs.fullerton.edu/cpsc485/editdist.html
# David Feinzimer 4168
#Requirements
#   Python 3.x
#Instructions
#   In project directory run python3 main.py

from array import *

edit_distance = None
identical = False
word_one = None
word_two = None

# Check to see if the two words are identical
def check_identical():
    if word_one == word_two:
        print("The two words are identical")
        identical = True
        set_result(0, word_one, word_two)
        return True

# Print results out
def set_result(a, b, c):
    print("Edit distance: " + str(a))
    print("Alignment:")
    print(b)
    print(c)

print("Welcome to Edit Distance Calculator")
print("This program calculates the edit distance between two words using dynamic programming.")
print("The lengths of the words should be less than 30 characters.")
print("Please input two words for the edit distance.")

word_one = input("The first word: ")
word_two = input("The second word: ")

print("You entered: " + word_one + " and " + word_two)

check_identical()
