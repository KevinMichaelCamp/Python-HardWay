# Square each value in a given array, returning that same array with changed values.

def squareArray(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] ** 2
    return arr

# Test Cases
print(squareArray([1,2,3,4,5,6]))
print(squareArray([1,-2,3,-4,5,6]))
