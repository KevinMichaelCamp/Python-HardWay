# Python - The Hard Way - Exercise 11 - Inputs

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you are %r years old, %r tall, and %r heavy." % (age, height, weight)

print "Enter a number."
x = int(raw_input())
print "And a number to add."
y = int(raw_input())
print x + y