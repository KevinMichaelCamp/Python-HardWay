# Given a string, return whether all contained letters are in alphabetical order.

def isAlphabetical(str):
    for i in range(1, len(str)):
        if str[i] < str[i-1]:
            return False

    else:
        return True

# Test Cases
print(isAlphabetical("abcdefg"))
print(isAlphabetical("abcsdfgf"))
