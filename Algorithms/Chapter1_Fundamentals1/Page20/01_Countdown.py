# Create a function that accepts a number as an input. Return a new
# array that counts down by one, from the number (as array's zero'th
# element) down to 0 (as the last element). How long is this array?

def countdown(num):
    arr = []

    for i in range(num, -1, -1):
        arr.append(i)

    return arr, len(arr)

# Test Cases
print(countdown(9))

