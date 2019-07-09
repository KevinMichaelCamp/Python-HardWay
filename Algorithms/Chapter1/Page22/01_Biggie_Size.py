# Given an array, write a function that changes all positive numbers
# in the array to "big". Example: makeItBig([-1,2,5,-5]) returns the
# same array, changed to [-1,"big","big",-05].

def makeItBig(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = "big"
    return arr

# Test Cases
print(makeItBig([-1,3,5,-5]))
