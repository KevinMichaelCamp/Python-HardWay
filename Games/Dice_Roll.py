import random
import time

min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    time.sleep(1)
    print("Rolling the die...")
    time.sleep(.1)
    print(".")
    time.sleep(.1)
    print(".")
    time.sleep(.1)
    print(".")
    time.sleep(.1)
    print(".")
    time.sleep(.1)
    print(".")
    time.sleep(.1)
    print(".")
    print("The values are...")
    time.sleep(1)
    print(random.randint(min, max))
    print(random.randint(min, max))

    roll_again = input("Roll the die again?")
