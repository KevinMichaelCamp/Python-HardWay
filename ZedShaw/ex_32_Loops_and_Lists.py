# Python - The Hard Way - Exercise 32 - Loops & Lists

count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in count:
    print("This is count %d." % number)

for fruit in fruits:
    print("A fruit of type %s." % fruit)

for i in change:
    print("I got %r." % i)

# building lists
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print("Adding %d to the list." % i)
    # append all i in range
    elements.append(i)

print(elements)

# now we can print them count
for i in elements:
    print("Element is: %d." % i)
