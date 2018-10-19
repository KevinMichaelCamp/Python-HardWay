# Python - The Hard Way - Exercise 13 - Parameters, Unpacking, Variables

from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
#print length of argv
print("Number of arguments", len(argv))

fourth = input("Enter fourth variable... ")
print(fourth)
