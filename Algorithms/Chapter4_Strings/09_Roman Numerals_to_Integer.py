# Given a string containinga Roman Numeral representation of a positive integer, return the integer.

def romanNumeralToInteger(str):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0

    for i in range(len(str)):
        if i > 0 and rom_val[str[i]] > rom_val[str[i-1]]:
            integer += rom_val[str[i]] - 2 * rom_val[str[i-1]]
        else:
            integer += rom_val[str[i]]

    return integer


# Test Cases
print(romanNumeralToInteger("MMMCMLXXXVI"))
