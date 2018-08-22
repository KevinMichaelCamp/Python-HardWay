# Python - The Hard Way - Exercise 17 - More Files
from sys import argv
#import exists
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s." % (from_file, to_file)

# We could do these on one line
in_file = open(from_file)
indata = in_file.read()

# print size of file with len(file)
print "The input file is %d bytes long." % len(indata)

# Check to see if output file exists
exists(to_file)

# Write to to_file(out_file)
out_file = open(to_file, 'w')
out_file.write(indata)

print "Allright, all done."

#close both files
out_file.close()
in_file.close()
