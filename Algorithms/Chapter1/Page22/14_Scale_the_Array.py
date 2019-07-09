# Given array arr and the number num, multiply each arr value by num, and return the changed array.

def scaleArray(arr, num):
    for i in range(len(arr)):
        arr[i] = arr[i] * num
    return arr

# Test Cases
print(scaleArray([1,2,3,4,5], 3))
