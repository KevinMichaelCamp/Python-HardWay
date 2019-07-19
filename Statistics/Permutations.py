"""
Permutations
Often, we want to count all of the possible ways that a single set of objects can be arranged. For example, consider the letters X, Y, and Z. These letters can be arranged a number of different ways (XYZ, XZY, YXZ, etc.) Each of these arrangements is a permutation.

A permutation is an arrangement of all or part of a set of objects, with regard to the order of the arrangement. This means that XYZ is considered a different permutation than ZYX.
The number of permutations of n objects taken r at a time is denoted by nPr.
Rule 2. The number of permutations of n objects taken r at a time is

nPr = n(n - 1)(n - 2) ... (n - r + 1) = n! / (n - r)!
"""

# Factorial Function
def factorial(num):
    factorial = 1

    for i in range(num, 0, -1):
        factorial *= i
    return factorial

def permutations(n, r):
    permutations = factorial(n) // factorial(n-r)
    return permutations

"""
Example
In horse racing, a trifecta is a type of bet. To win a trifecta bet, you need to specify the horses that finish in the top three spots in the exact order in which they finish. If eight horses enter the race, how many different ways can they finish in the top three spots?

Solution: Rule 2 tells us that the number of permutations is n! / (n - r)!. We have 8 horses in the race. so n = 8. And we want to arrange them in groups of 3, so r = 3. Thus, the number of permutations is 8! / (8 - 3)! or 8! / 5!. This is equal to (8)(7)(6) = 336 distinct trifecta outcomes. With 336 possible permutations, the trifecta is a difficult bet to win.

8P3 = 8! / (8 - 3)! or 8! / 5! = (8)(7)(6) = 336
"""

print(f"{permutations(8,3): ,}")
