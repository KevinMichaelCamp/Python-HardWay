# Swap positions of succesive pairs of values in a given array. If length is odd, do not change the final element. For [1,2,3,4], return [2,1,4,3]. Change ["Brendan", True, 42] to [True, "Brendan", 42].  No built-positions

def swapPairs(arr):
    for i in range(0, len(arr)-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

# Test Cases
print(swapPairs([1,2,3,4]))
print(swapPairs(["Brendan", True, 42]))
