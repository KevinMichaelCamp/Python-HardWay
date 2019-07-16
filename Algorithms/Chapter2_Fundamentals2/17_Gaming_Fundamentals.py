# 1. Create function rollOne() to return a randomly selected integer between 1 and 6 (inclusive)
# 2. Create a function playFives(num), which should call rollOne() num times, printing the value rollOne returns and if 5 is returned print "That's good luck!"
# 3. Create function playStatitics(), which should call rollOne() 8 times, and print out the lowest and highest roll after 8 rolls.
# 4. Create playStatitics2() that also prints the sum of the rolls.
# 5. Create playstatistics3(num) that rolls num number of times.
# 6. Create playStatitics4(num) that returns the average rolls
# 7. Just create 1 playStatitics(num) that does 3-6
import random

def rollOne():
    return random.randint(1,6)

def playFives(num):
    for i in range(num):
        roll = rollOne()
        print(roll)
        if roll == 5:
            print("That's lucky!")

def playStatitics(num):
    # Roll dice num times
    rolls = []

    for i in range(num):
        rolls.append(rollOne())

    # Statistics
    max = rolls[0]
    min = rolls[0]
    sum = 0

    for j in range(len(rolls)):
        sum += rolls[j]
        avg = sum // len(rolls)
        if rolls[j] > max:
            max = rolls[j]
        if rolls[j] < min:
            min = rolls[j]

    print("Game Statistics", '\n', "*"*50, '\n', "Sum:", sum, "Average:", avg, "High Roll:", max, "Low Roll:", min)




# Test Cases
# playFives(5)
playStatitics(52)
