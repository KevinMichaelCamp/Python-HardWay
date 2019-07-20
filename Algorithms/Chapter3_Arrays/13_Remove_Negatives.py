# Create a function that accepts an array, removes the negative values, and returns the same array.

def removeNegatives(arr):
    i = 0

    while i < len(arr):
        if arr[i] < 0:
            del arr[i]
            i -= 1
        i += 1

    return arr

# Test Cases
print(removeNegatives([1,2,-3,4,-5,6]))
