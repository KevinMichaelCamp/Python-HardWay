# Given a Positive integer that is less than 4000, return a string containing that value in Roman Numeral representation. I=1, V=5, X=10, L=50, C=100, D=500, M=1000. Remember 4 is IV, 349 is CCCXLIX and 444 is CDXLIV.

def integerToRomanNumeral(int):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    roman_numeral = ""
    i = 0
    while int > 0:
        for _ in range(int // val[i]):
            roman_numeral += symbols[i]
            int -= val[i]
        i += 1

    return roman_numeral


# Test Cases
print(integerToRomanNumeral(4))
print(integerToRomanNumeral(349))
print(integerToRomanNumeral(444))
print(integerToRomanNumeral(1999))
print(integerToRomanNumeral(3449))
