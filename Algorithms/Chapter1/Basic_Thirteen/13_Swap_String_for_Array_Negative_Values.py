# Given an array of numbers, replace any negative values with the string "Dojo".

def swapStringForNegative(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = "Dojo"
    return arr

# Test Cases
print(swapStringForNegative([1,2,-3,4,5,-6]))
