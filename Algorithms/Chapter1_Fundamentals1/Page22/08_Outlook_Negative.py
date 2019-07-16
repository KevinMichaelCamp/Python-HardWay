# Given an array, create and return a new one containing all the values of the provided array, made negative (not simply multiplied by - 1). Given [1,-3,5], return [-1,-3,-5].

def makeNegative(arr):
    new_arr = []

    for i in range(len(arr)):
        if arr[i] <= 0:
            new_arr.append(arr[i])
        else:
            new_arr.append(-(arr[i]))
    return new_arr

# Test Cases
print(makeNegative([1,-3,5]))
