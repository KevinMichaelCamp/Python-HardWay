# Given a number of any size, return the most significant digit. Use while to bring the most significant digit into range where modulus can be used. The most significant digit is the leftmost non-zero digit of a number. Given 12345 return 1, Given 67.89 return 6, given .00987, return 9. Handle negative num values as well.

def mostSigDigit(num):
    if num > 0:
        if num >= 1:
            while num >= 10:
                num = num / 10
        else:
            while num < 1:
                num =  num * 10
        return int(num % 10)

    else:
        if num <= -1:
            while num <= -10:
                num = num / 10
        else:
            while num > -1:
                num = num * 10
        return int(num % -10)


# Test Cases
print(mostSigDigit(12345))
print(mostSigDigit(67.89))
print(mostSigDigit(.00987))
print(mostSigDigit(-12345))
print(mostSigDigit(-67.89))
print(mostSigDigit(-.00987))
