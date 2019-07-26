# Write a function that accepts as a parameter a string containing someone's name. Return a string containing the cool greeting: strip off the first letter of the name, capitalize the new word and add " to the [first letter]!" Given "Dylan" return "Ylan to the D!"

def unctionToTheF(str):
    greeting = str[1:].capitalize()
    greeting += " to the "
    greeting += str[0]
    greeting += "!"
    return greeting

# Test Cases
print(unctionToTheF("Dylan"))
print(unctionToTheF("Kevin"))
