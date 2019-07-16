# Return any given array, after setting any negative values to zero.

def zeroOutNegative(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = 0
    return arr

# Test Cases
print(zeroOutNegative([1,2,-3,4,-5,6,7]))
