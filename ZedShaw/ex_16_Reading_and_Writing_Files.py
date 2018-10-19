# Python - The Hard Way - Exercise 16 - Reading & Writing Files

# from sys module import argument variable
from sys import argv
# list 2 arguments
script, filename = argv

print "We are going to erase %r." % filename
print "If you DO NOT want to do that, hit CTRL-C (^C)."
print "If you DO want that, hit RETURN."
# User input
raw_input("?")

# opening file in write mode (necessary to enable truncate)
print "Opening the file..."
target = open(filename, 'w')

# truncate (erase) file (not necessary with write mode)
print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I am going to write these to the file."

# cleaner code - use strings, formatting, and escapes to simplify to 1 line
target.write("%s\n%s\n%s\n" % (line1, line2, line3))

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print "And finally, we close it."
target.close()
