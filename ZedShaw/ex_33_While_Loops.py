# Python - The Hard Way - Exercise 33 - While-Loops

i = 0
numbers = []

while i < 6:
    print("At the top i is %d." % i)
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print("At the bottom of i is %d." % numbers[0])

print(numbers)
print("The numbers: ")
for num in numbers:
    print(num)
