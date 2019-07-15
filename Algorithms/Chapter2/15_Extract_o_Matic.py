# Create the function extractDigit(num, digitNum) function that given a number and a digit number, returns the numeral value of that digit. 0 represents the ones digit, 1 represents the tens digit, etc. Given (1824, 2) return 8. Given (123.45, -1) return 4. Handle negative num values as well.

def extractDigit(num, digitNum):
    extract = num / (10**digitNum)

    if num >= 0:
        return (int(extract % 10))
    else:
        return (int(extract % -10))

# Test Cases
print(extractDigit(1824, 2))
print(extractDigit(123.45, -1))
print(extractDigit(-1824, 2))
