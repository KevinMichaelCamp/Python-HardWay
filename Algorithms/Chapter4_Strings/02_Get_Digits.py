# Given a string, return the integer made from the string's digits. Given "0s1a3y5w7h9a2t4?6!8?0" return 1357924680.

import re

DIGIT_REGEX = re.compile(r'([0-9])')

def getDigits(string):
    digit_string = ""
    for char in string:
        if DIGIT_REGEX.match(char):
            digit_string += char

    return int(digit_string)

# Test Cases

print(getDigits("0s1a3y5w7h9a2t4?6!8?0"))
