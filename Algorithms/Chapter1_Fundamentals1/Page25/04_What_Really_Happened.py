# The chance of one disaster is unrelated to another...Change whatHappensToday() to whatReallyHappens(). Test for each disaster independently. On a given day, all 5 disasters could happen. Or none.

import random

def whatReallyHappens():
    disasters = []

    if random.random() < .1:
        disasters.append('volcano')

    if random.random() < .15:
        disasters.append('tsunami')

    if random.random() < .20:
        disasters.append('earthquake')

    if random.random() < .25:
        disasters.append('earthquake')

    if random.random() < .30:
        disasters.append('earthquake')

    return disasters

# Test Cases
print(whatReallyHappens())
