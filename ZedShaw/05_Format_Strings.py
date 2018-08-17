# Python - The Hard Way - Exercise 5 - Format Strings

name = "Kevin Michael Camp"
age = 38  # 11.20.1979
height = 75  # inches
weight = 215  # lbs
eyes = 'Hazel'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's weighs %d lbs." % weight
print "Almost right for his height!"
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are %s, now that he went to the dentist." % teeth

# tricky line
print "If I add %d, %d, and %d - I get %d." % (
    age, height, weight, age + height + weight)

print "I have %r hair and am %r inches tall." % (hair, height)

# Metric Conversions
weight_kilo = weight * 0.45359237
height_cm = height * 2.54

print "My weight in kilograms is %d kg." % weight_kilo
print "My height in centimeters is %d cm." % height_cm

pi = 3.14159265359
pi_rounded = round(pi)
print "%f rounded is %f." % (pi, pi_rounded)
