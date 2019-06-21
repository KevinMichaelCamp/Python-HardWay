#import time module
import time

name = input("What is your name?")

print("Hello, " + name + "! Time to play hangman!")

time.sleep(10)

print("Start guessing...")

word = "secret"

guesses = ''

turns = 10

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char)
        else:
            print("-")
            failed += 1

    if failed == 0:
        print("You win!")
        print("The word was " + word)
        break

    guess = input("Guess a character:")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong guess")

        if turns == 0:
            print("You lose!")
