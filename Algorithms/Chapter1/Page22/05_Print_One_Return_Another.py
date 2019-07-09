# Build a function that takes array of numbers. The function should print second-to-last value in the array, and return first odd value in the array.

def printOneReturnAnother(arr):
    print(arr[-2])
    for num in arr:
        if num % 2 != 0:
            return num

# Test Cases
print(printOneReturnAnother([2,4,-3,5,3,8]))
