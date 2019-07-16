# Given array, remove and return the first value at the beginning of the array. Do this without using any built-in methods, e.g. (.pop(index))

def popFront(arr):
    pop = arr[0]
    arr = arr[1:]
    return pop, arr

# Test Cases
print(popFront([1,2,3,4,5]))
