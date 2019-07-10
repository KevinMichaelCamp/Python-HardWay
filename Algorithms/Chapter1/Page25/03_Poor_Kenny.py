# Out of the last 100 days, there were 10 days with volcanoes, 15 with tsunamis, 20 earthquakes,  25 blizzards, and 30 meteors (for 100 days total). If these probabilities continue, write whatHappensToday() to predict a day's outcome.
import random

def whatHappensToday():
    randNum = random.randint(1,100)

    if randNum > 70:
        return 'meteor'
    elif randNum > 45:
        return 'blizzard'
    elif randNum > 25:
        return 'earthquake'
    elif randNum > 10:
        return 'tsunami'
    else:
        return 'volcano'

print(whatHappensToday())
