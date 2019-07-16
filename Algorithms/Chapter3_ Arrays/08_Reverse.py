# Given a numerical array, reverse the order of values, in-place.

def reverseArray(arr):
    for i in range(len(arr)//2):
        arr[i], arr[-i-1] = arr[-i-1], arr[i]
    return arr

# Test Cases
print(reverseArray([1,2,3,4,5,6]))
print(reverseArray([1,5,6,4,8,3,4]))
