# Create threesFives() that adds values from 100 to 4000000 (inclusive) if that value is evenly divisible by 3 or 5, but not both. Display the final sum in the console

# Create betterThreesFives(start, end) that allows you to enter arbitrary start and end values for the range

def threesFives():
    total = 0

    for num in range(100, 4000001):
        if num % 3 == 0 and num % 5 == 0:
            continue
        elif num % 3 == 0 or num % 5 == 0:
            total += num

    return total

# Test Cases
print(threesFives())


def betterThreesFives(start, end):
    total = 0

    for num in range(start, end + 1):
        if num % 3 == 0 and num % 5 == 0:
            continue
        elif num % 3 == 0 or num % 5 == 0:
            total += num

    return total

# Test Cases
print(betterThreesFives(1, 20))
