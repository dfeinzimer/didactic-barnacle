# Version 11.11.18.5
# Adapted from http://wang.ecs.fullerton.edu/cpsc485/editdist.html
# David Feinzimer 4168
# Requirements
#    Python 3.x
# Instructions
#    No compilation necessary
#    In project directory run python3 main.py

matrix = []


# Finds the optimal global alignment
def find_alignment():
    b = []  # Word one alignment
    c = []  # Word two alignment
    row = len(word_one)
    column = len(word_two)
    while len(b) != len(word_one):
        if word_one[row - 1] == word_two[column - 1]:
            b.insert(0, word_one[row - 1])
            c.insert(0, word_two[column - 1])
            column -= 1
            row -= 1
        elif matrix[row][column] - 1 == matrix[row - 1][column - 1]:
            b.insert(0, word_one[row - 1])
            c.insert(0, word_two[column - 1])
            column -= 1
            row -= 1
        elif matrix[row][column] - 1 == matrix[row][column - 1]:
            b.insert(0, '_')
            c.insert(0, word_two[column - 1])
            column -= 1
        elif matrix[row][column] - 1 == matrix[row - 1][column]:
            b.insert(0, word_one[row - 1])
            c.insert(0, '_')
            row -= 1
    set_result(matrix[len(word_one)][len(word_two)], b, c)


# Fills the matrix with correct values
def fill_matrix():
    for row_counter in range(len(word_one)):
        for column_counter in range(len(word_two)):
            if word_one[row_counter] == word_two[column_counter]:
                matrix[row_counter + 1][column_counter + 1] = matrix[row_counter][column_counter]
            else:
                matrix[row_counter + 1][column_counter + 1] = min(matrix[row_counter + 1][column_counter],
                                                                  matrix[row_counter][column_counter],
                                                                  matrix[row_counter][column_counter + 1]) + 1


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
    print("The matrix:")
    print('    ', end='')
    for i in range(len(word_two)):
        print(word_two[i], end='  ')
    print()
    row_num = 0
    for r in matrix:
        if row_num == 0:
            print(' ', end='')
        else:
            print(word_one[row_num-1], end='')
        row_num += 1
        for col in r:
            print(col, end='  ')
        print()  # Newline
        print()  # Spacing


# Print results out
def set_result(a, arg_b, arg_c):
    print("The edit distance is: " + str(a))
    print()
    print("Alignment is:")
    for i in range(len(arg_b)):
        print(arg_b[i], end='')
    print()
    for i in range(len(arg_c)):
        print(arg_c[i], end='')
    print()


print("Welcome to Edit Distance Calculator")
print("This program calculates the edit distance between two words using dynamic programming.")
print("The lengths of the words should be less than 30 characters.")
print("Please input two words for the edit distance.")

word_one = input("The first word: ")
word_two = input("The second word: ")
print()

initialize_matrix()

fill_matrix()

print_matrix()

find_alignment()
