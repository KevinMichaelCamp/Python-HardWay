# Python - The Hard Way - Exercise 20 - Functions & Files

# import argv and set
from sys import argv
script, input_file = argv

# define print function
def print_all(f):
    print f.read()

# define rewind function
def rewind(f):
    f.seek(0)

# define print_a_line function
def print_a_line(line_count, f):
    print line_count, f.readline()

# open input_file
current_file = open(input_file)

print "First, let's print the whole file:\n"

# print file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# rewind file
rewind(current_file)

print "Let's print three lines:"

# print by line
current_line = 1
print_a_line(current_line, current_file)    # line 1

current_line = current_line + 1
print_a_line(current_line, current_file)    # line 2

current_line = current_line + 1
print_a_line(current_line, current_file)    # line 3
