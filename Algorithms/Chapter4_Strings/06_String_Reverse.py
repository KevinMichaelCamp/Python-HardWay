# Implement reverseString(str) that given a string, returns that string with reversed characters. Given "creature" return "erutaerc". Do not user built ins.


# Option 1: Reversing a Python String With the “[::-1]” Slicing Trick

def reverseString(str):
    str = str[::-1]
    return str


# Test Cases
print(reverseString("creature"))



# Option 2: Reversing a Python String Using  reversed() and str.join()
def reverseString(str):
    return "".join(reversed(str))

# Test Cases
print(reverseString("creature"))
