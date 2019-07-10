# Fill in the Blank Game - Ask user's name, then refer to user by name as you ask them a series of questions. At exit print the statistics of the game to the console: user name, number of qustions answered and number right.

import time

num_questions = 0
num_correct = 0

def sleep():
    time.sleep(1)

print("Welcome to the Fill in the Blank game!")
sleep()
name = input("What is your name? ")
sleep()
print("Hello", name, "let's play a game.")
sleep()

# Question Function
def question(question, answer):
    global num_correct
    global num_questions

    num_questions += 1
    sleep()
    print(question)
    guess = input(">")
    sleep()
    if guess == answer:
        num_correct += 1
        print("Correct!")
    else:
        print("Wrong!")
    sleep()

question("How many donuts are in a baker's dozen?", "13")
question("What year is the next leap year?", "2020")
question("How many is a couple?", "2")

sleep()
print("Game Stats:", '\n', "User name:", name, '\n', "Questions:", num_questions,'\n', "Number correct:", num_correct)
