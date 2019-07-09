#  Create a function that takes an array of numbers.  The function should print the lowest value in the array, and return the highest value in the array.

def printLowReturnHigh(arr):
    low = arr[0]
    high = arr[0]

    for i in range(len(arr)):
        if i < low:
            low = arr[i]
        elif i > high:
            high = arr[i]

    print(low)
    return high

# Test Cases
print(printLowReturnHigh([-5,2,4,2,-4,9]))
