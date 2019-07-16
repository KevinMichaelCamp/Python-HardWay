# Given an array and a value Y, count and print the number of array values greater than Y.

def greaterThanY(arr, Y):
    count = 0
    for num in arr:
        if num > Y:
            count += 1
    return count

# Test Cases
print(greaterThanY([1,2,3,4,5,6], 3))
