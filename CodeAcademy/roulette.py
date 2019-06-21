import random
import sys
import time

# Get random roulette spin variables
def spin():
    num = random.randint(-1, 36)

    if num == -1:
        num = 0

    # Even/Odd
    if num <= 0:
        evenOdd = "zero"
    elif num % 2 == 0:
        evenOdd = "even"
    else:
        evenOdd = "odd"

    # Black/Red
    if num <= 0:
        color = "green"
    elif ((num <= 10) or (num >= 19 and num <= 28)) and num % 2 == 0:
        color = "black"
    elif ((num >= 11 and num <= 18) or (num >= 29)) and num % 2 != 0:
        color = "black"
    else:
        color = "red"

    return num, evenOdd, color

# Place bets
def place_bets(bet, call):
    global money
    num, evenOdd, color = spin()
    print(color.capitalize() + " " + str(num))

    # Number Bet
    if type(call) == int:
        odds = 35
        if call == num:
            winnings = bet * odds
            money += winnings
            print("Holy shit, right on the nose!!!")
            time.sleep(1)
            print("You win $" + str(winnings))
            time.sleep(1)
            print("You now have $" + str(money))
        else:
            money -= bet
            print("Sorry, buster. You lose $" + str(bet))
            time.sleep(1)
            print("You now have $" + str(money))

    # Even/Odd Bet
    elif str.lower(call) == 'even' or str.lower(call) == 'odd':
        if str.lower(call) == evenOdd:
            money += bet
            print("It's your lucky day!")
            time.sleep(1)
            print("You win $" + str(bet))
            time.sleep(1)
            print("You now have $" + str(money))
        else:
            money -= bet
            print("Sorry, buster. You lose $" + str(bet))
            time.sleep(1)
            print("You now have $" + str(money))

    # Black/Red Bet
    elif str.lower(call) == 'black' or str.lower(call) == 'red':
        if str.lower(call) == color:
            money += bet
            print("It's your lucky day!")
            time.sleep(1)
            print("You win $" + str(bet))
            time.sleep(1)
            print("You now have $" + str(money))
        else:
            money -= bet
            print("Sorry, buster. You lose $" + str(bet))
            time.sleep(1)
            print("You now have $" + str(money))

    else:
        print("Invalid input...")

# Play Roulette
time.sleep(1)
print("Welcome to the Roulette table!!!")
time.sleep(1)
print("What is your name?")
name = input()
time.sleep(1)
print("Hello, " + name + ".")
time.sleep(1)
print("How much cash would you like from the ATM?")
money = int(input())
time.sleep(1)
# Roulette Function
def play_roulette():
    print("How much would you like to wager?")
    bet = int(input())
    time.sleep(1)

    # Check if user had enough money for bet
    if bet > money:
        print("You don't have enough money, bucko...")
        sys.exit()

    print("Where would you like to place your bet?")
    time.sleep(1)
    print("You can bet on red or black, which pays 1:1")
    time.sleep(1)
    print("You can bet on odd or even, which pays 1:1")
    time.sleep(1)
    print("Or if you are feeling lucky, you can bet on a number, which pays 35:1")
    time.sleep(1)
    print("So what'll it be?")
    call = input()
    # Change bet to type int if number entered

    if len(call) <= 2:
        call = int(call)

    string = "Spinning roulette wheel..."
    for i in string:
        print(i, end="")
        time.sleep(.1)
        sys.stdout.flush()
    place_bets(bet, call)

    # Check to see if User has any money
    if money == 0:
        print("Sorry, you are outta cash...")
        sys.exit()

    print("Would you like to play again?")
    playAgain = input()
    if str.lower(playAgain) == "yes" or str.lower(playAgain) == "y":
        play_roulette()
    else:
        time.sleep(1)
        print("Thanks for playing, bye!")

play_roulette()
