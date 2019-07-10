# Given an array, move all values forward by one index, dropping the first and leaving a '0' value at the end.

def shiftValues(arr):
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
        print(arr)
    arr[-1] = 0
    return arr

#Test Cases
print(shiftValues([1,2,3,4,5,6]))
