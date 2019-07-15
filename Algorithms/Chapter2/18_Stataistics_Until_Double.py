# Implement a 20-sided die. Roll until you get a value twice in a row. Display number of rolls, min, max, and average.

import random

def twentySidedDie():
    return random.randint(1,20)

def twiceInaRow():
    rolls = []
    for i in range(2):
        rolls.append(twentySidedDie())

    i = 0
    while rolls[i] != rolls[i+1]:
        rolls.append(twentySidedDie())
        i += 1

    # Statistics
    max = rolls[0]
    min = rolls[0]
    sum = 0
    count = 0

    for i in range(len(rolls)):
        count += 1
        sum += rolls[i]
        if rolls[i] > max:
            max = rolls[i]
        if rolls[i] < min:
            min = rolls[i]
    avg = round(sum / len(rolls))

    print("Game Statistics:", '\n', '*'*25,'\n')
    print(rolls, '\n', "Rolls:", count, "Sum:", sum, "Average:", avg, "High Roll:", max, "Low Roll:", min)



twiceInaRow()
