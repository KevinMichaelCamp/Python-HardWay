# Python - The Hard Way - Exercise 31 - Making Decisions

print("You enter a dark room with two doors. Do you go through door #1 or door #2?")

door = input("> ")

if door == '1':
    print("There's a giant bear here eating a cheese cake. What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == '1':
        print("The bear eats your face off. YOUR DEAD!!!")
    elif bear == '2':
        print("The bear eats your legs off. Crawl Away!!!")
    else:
        print(("Well, doing %s is probably better. Bear runs away." % bear))

elif door == '2':
    print("You stare into the endless abyss at Chtulu's retina.")
    print("1. Throw doll at Chtulu.")
    print("2. Kick Chtulu's eye.")
    print("3. Kiss Chtulu.")

    chtulu = input("> ")

    if chtulu == '1' or chtulu == '2':
        print("Bad choice. Chtulu melts your brain.")
    elif chtulu == '3':
        print("Aww. You love Chtulu. You have many hideous devil babies!")
    else:
        print("Whatever you did, it pissed Chtulu off.")

else:
    print("You stumble around and fall on a knife and die!!")
