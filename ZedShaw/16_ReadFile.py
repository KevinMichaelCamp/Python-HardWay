from sys import argv

script, filename = argv

print "Now I will read the changed file."
print "Hit ENTER to continue."

raw_input("Hit Enter")

print "Opening file."

target = open(filename)

print "Reading file."

print target.read()

print "Closing file."

target.close()
