# Create a function that, given a string, returns all of the string's content without the spaces. Given "Pl ay  Th a t Fu nk  y Mus ic" return "PlayThatFunkyMusic".

def removeSpaces(string):
    for char in string:
        string = string.replace(' ', '')

    return string

# Test Cases
print(removeSpaces("Pl ay  Th a t Fu nk  y Mus ic"))
