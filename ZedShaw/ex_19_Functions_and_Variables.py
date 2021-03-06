# Python - The Hard Way - Exercise 19 - Functions & Variables

# Define function - will be called 4 times using different
# input methods


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheese." % cheese_count)
    print("You have %d boxes of crackers." % boxes_of_crackers)
    print("Man, that's enough for a party!")
    print("Get a blanket.\n")


# Direct input
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# Input using variables
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Input using math
print("We can even do the math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Input using variables & math
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
