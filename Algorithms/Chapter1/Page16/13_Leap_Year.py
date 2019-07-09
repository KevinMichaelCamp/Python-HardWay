# Write  a function that determines whether a given year is a leap year.
# If a year is divisible by four, it is a leap year, unless it is
# divisible by 100. However if it divisible by 400, then it is.

def leapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# Test Cases
print("Testing year 2020")
print(leapYear(2020))
print('\n')
print("Testing year 100")
print(leapYear(100))
print('\n')
print("Testing year 400")
print(leapYear(400))
print('\n')
print("Testing year 2017")
print(leapYear(2017))
