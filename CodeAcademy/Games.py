import random
import sys
import time

# USER - Game Interface
print("Welcome to the Casino!")
time.sleep(1)
print("What is your name? ")
name = input()
time.sleep(1)
print("Hi " + name + ", how much cash would you like from the ATM?")
money = int(input())
time.sleep(1)

# COIN FLIP GAME
# Flip Coin function
def flip_coin():
    randnum = random.randint(0,1)

    if randnum == 0:
        outcome = "heads"
    else:
        outcome = "tails"

    return outcome

# Call Coin function
def call_coin_flip(bet, call):
    flip = flip_coin()
    global money

    if str.lower(call) == flip:
        money += bet
        print(str.upper(flip) + "! You win " + str(bet) + ".")
        print("Total Moneys - $" + str(money))
    else:
        money -= bet
        print(str.upper(flip) + "! You lose " + str(bet) + ".")
        print("Total Moneys  $" + str(money))

# Coin Flip Game function
def play_coin_flip():
    print("How much would you like to bet?")
    bet = int(input())
    if money < bet:
        print("You don't have enough money")
        play_game()
    time.sleep(1)
    print("Heads or tails?")
    call = input()
    string = "Flipping coin"

    for char in string:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(.25)

    sys.stdout.write("\n")
    call_coin_flip(bet, call)
    time.sleep(1)
    if money == 0:
        print("Sorry, you are broke!")
        sys.exit()
    else:
        print("Would you like to play again?")
        playAgain = input()
        if str.lower(playAgain) == "y" or str.lower(playAgain) == "yes":
            play_game()
        else:
            time.sleep(1)
            print("Thanks for playing. Bye")

# CHO-HAN GAME
# Dice Roll Function
def dice_roll():
    string = "Rolling dice"
    for char in string:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(.25)
    sys.stdout.write("\n")
    die1 = random.randint(1,9)
    print("Die 1 roll - " + str(die1))
    time.sleep(1)
    die2 = random.randint(1,9)
    print("Die 2 roll - " + str(die2))
    sum = die1 + die2

    if sum % 2 == 0:
        roll = "even"
    else:
        roll = "odd"

    time.sleep(1)
    print("Sum of dice roll is " + str(sum) + " - " + roll)
    return roll

# Cho-Han Function
def cho_han(bet, call):
    global money
    roll = dice_roll()

    if str.lower(call) == roll:
        money += bet
        print("You win $" + str(bet) + "!")
        print("Total Moneys  $" + str(money))
    else:
        money -= bet
        print("You lose $" + str(bet) + "!")
        print("Total Moneys  $" + str(money))

    time.sleep(1)
    if money == 0:
        print("Sorry, you are broke!")
        sys.exit()
    else:
        print("Would you like to play again?")
        playAgain = input()
        if str.lower(playAgain) == "y" or str.lower(playAgain) == "yes":
            play_game()
        else:
            time.sleep(1)
            print("Thanks for playing. Bye")

def play_cho_han():
    print("How much would you like to bet?")
    bet = int(input())
    if money < bet:
        print("You don't have enough money")
        play_game()
    time.sleep(1)
    print("Even or odd?")
    call = input()

    cho_han(bet, call)

# USER - Choose game
def play_game():
    print("What game would you like to play?")
    time.sleep(1)
    print("1. Coin Flip")
    time.sleep(1)
    print("2. Cho-Han")
    game = int(input())
    if game == 1:
        play_coin_flip()
    elif game == 2:
        play_cho_han()
    else:
        print("Invalid selection")
        play_game()

play_game()
