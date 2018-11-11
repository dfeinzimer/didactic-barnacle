#Version 11.11.18.1
# Adapted from http://wang.ecs.fullerton.edu/cpsc485/editdist.html
# David Feinzimer 4168
# Requirements
#    Python 3.x
# Instructions
#    In project directory run python3 main.py

from array import *

edit_distance = None
identical = False
matrix = []
word_one = None
word_two = None

# Check to see if the two words are identical
def check_identical():
    if word_one == word_two:
        print("The two words are identical")
        identical = True
        set_result(0, word_one, word_two)
        return True

# Builds an empty matrix with the correct number of rows and columns
def initialize_matrix():
    matrix.append([])  # Add header row
    for i in range(len(word_two) + 1):  # Fill header row
        matrix[0].append(i)
    for i in range(len(word_one)):  # Fill first column
        matrix.append([])
        matrix[i+1].append(i+1)
        for j in range(len(word_two)):
            matrix[i+1].append(0)

# Iterates through and prints matrix
def print_matrix():
    print('    ',end='')
    for i in range(len(word_two)):
        print(word_two[i],end='  ')
    print()
    row = 0
    for r in matrix:
        if row == 0:
            print(' ', end='')
        else:
            print(word_one[row-1], end='')
        row += 1
        for c in r:
            print(c, end='  ')
        print()  # Newline
        print()  # Spacing

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
print()

check_identical()

initialize_matrix()

print_matrix()

for row in range(len(word_one)):
    for column in range(len(word_two)):
        print("Comparing " + word_one[row] + " and " + word_two[column])
        if word_one[row] == word_two[column]:
            print("Match found")
            matrix[row+1][column+1] = matrix[row][column]
            print_matrix()
        else:
            print("Match not found")
            print("Using " + str(min(matrix[row+1][column], matrix[row][column], matrix[row][column+1])) + " +1 for new entry")
            matrix[row+1][column+1] = min(matrix[row+1][column], matrix[row][column], matrix[row][column+1]) + 1
            print_matrix()

print("Evaluation complete")
print_matrix()
