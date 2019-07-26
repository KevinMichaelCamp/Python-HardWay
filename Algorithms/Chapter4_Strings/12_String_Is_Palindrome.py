# Create a function that returns a boolean whether the string is a strict palindrome. For "a x a" or "racecar" return True. Do not ignore spaces, punctuation, or capitalization: if given "Dud" or "o ho" return False.

def isPalindrome(str):
    for i in range(len(str)//2):
        if str[i] == str[-i-1]:
            continue
        else:
            return False

    return True


# Test Cases
print(isPalindrome("racecar"))
print(isPalindrome("a x a"))
print(isPalindrome("Dud"))
print(isPalindrome("o ho"))



# Now DO ignore white space, capitalization, and punctiuation
import re

LETTER_REGEX =  re.compile(r'[a-zA-Z]')

def isPalindrome(str):
    just_char = ""
    for char in str:
        if LETTER_REGEX.match(char):
            just_char += char

    for i in range(len(just_char)//2):
        if just_char[i].lower() == just_char[-i-1].lower():
            continue
        else:
            return False

    return True



# Test Cases
print(isPalindrome("racecar"))
print(isPalindrome("a x a"))
print(isPalindrome("Dud"))
print(isPalindrome("o ho"))
print(isPalindrome("THISAINT"))
