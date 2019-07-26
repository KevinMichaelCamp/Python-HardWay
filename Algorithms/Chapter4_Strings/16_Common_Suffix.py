# Write a function that, when given a word array, returns the largest suffix (word-end) that is common to all words in the array. For inputs ['deforestation', 'citation', 'conviction', 'incarceration'] return "tion". For ['nice', 'ice', 'baby'] return none.

import os

def commonSuffix(list_of_strings):
    reversed_strings = [''.join(s[::-1]) for s in list_of_strings]
    reversed_lcs = os.path.commonprefix(reversed_strings)
    lcs = ''.join(reversed_lcs[::-1])
    if len(lcs):
        return lcs
    else:
        return None

# Test Cases
print(commonSuffix(['deforestation', 'citation', 'conviction', 'incarceration']))
print(commonSuffix(['nice', 'ice', 'baby']))
