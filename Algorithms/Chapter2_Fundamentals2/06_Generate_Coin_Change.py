# Make a function makeChange(cents) that accepts a number of American cents, and compute and print how to represent that ammount with the smallest number of coins.

def makeChange(cents):
    dollars = cents // 100
    remainder = cents % 100
    half_dollars = remainder // 50
    remainder = remainder % 50
    quarters = remainder//25
    remainder = cents % 25
    dimes = remainder // 10
    remainder = remainder % 10
    nickels = remainder // 5
    remainder = remainder % 5
    pennies = remainder


    print(str(cents) + " cents can be represented by:")
    print("dollars:", dollars)
    print("half-dollars:", half_dollars)
    print("quarters:", quarters)
    print("dimes:", dimes)
    print("nickels:", nickels)
    print("pennies:", pennies)

# Test Cases
makeChange(94)
makeChange(23)
makeChange(321658)
