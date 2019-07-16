# Given an array of comparable values, move the lowest elementto array's front, shifting backward any elements previously ahead of it. Do not otherwise change the array's order. Given [4,2,1,3,5] return [1,4,2,3,5]

def removeAt(arr, index):
    pop = arr[index]
    arr = arr[:index] + arr[(index+1):]
    return pop

def insertAt(arr, index, value):
    arr = arr[:index] + [value] + arr[index:]
    return arr

def minToFront(arr):
    min = arr[0]
    minIndex = 0

    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
            minIndex = i

    removeAt(arr, minIndex)
    insertAt(arr, 0, min)
    return arr


print(minToFront([1,4,2,3,5]))
