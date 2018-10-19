# Python - The Hard Way - Exercise 15 - Reading Files

# import argv (Argument Variable) from sys module (system)
from sys import argv

# Argument Variables(2) = script(scriptname) & filename(.txt input file)
script, filename = argv

# Open file (filename) and store in variable (txt)
txt = open(filename)

# Read file (txt)
print("Here's your file %r:" % filename)
print(txt.read())

# Use raw_input to input filename (txt)
print("Type the filename again:")
file_again = input("~ ")

# Open file
txt_again = open(file_again)

# Read file
print(txt_again.read())

# Close files
txt.close
txt_again.close
