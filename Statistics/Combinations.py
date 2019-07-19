"""Combinations
Sometimes, we want to count all of the possible ways that a single set of objects can be selected - without regard to the order in which they are selected.

In general, n objects can be arranged in n(n - 1)(n - 2) ... (3)(2)(1) ways. This product is represented by the symbol n!, which is called n factorial. (By convention, 0! = 1.)
A combination is a selection of all or part of a set of objects, without regard to the order in which they were selected. This means that XYZ is considered the same combination as ZYX.
The number of combinations of n objects taken r at a time is denoted by nCr.

Rule 1. The number of combinations of n objects taken r at a time is

nCr = n(n - 1)(n - 2) ... (n - r + 1)/r! = n! / r!(n - r)!

"""

# Factorial Function
def factorial(num):
    factorial = 1

    for i in range(num, 0, -1):
        factorial *= i
    return factorial

# Combinations Function
def combinations(n, r):
    combinations = factorial(n) // (factorial(r) * factorial((n-r)))
    return combinations


"""Example
Five-card stud is a poker game, in which a player is dealt 5 cards from an ordinary deck of 52 playing cards. How many distinct poker hands could be dealt? (Hint: In this problem, the order in which cards are dealt is NOT important; For example, if you are dealt the ace, king, queen, jack, ten of spades, that is the same as being dealt the ten, jack, queen, king, ace of spades.)
"""
# Test Cases
print(f"{combinations(52, 5): ,}")
