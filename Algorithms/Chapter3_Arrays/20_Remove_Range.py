# Given array, and indices start and end, remove values in that index range. Given ([20,30,40,50,60,70], 2, 4) return [20, 30, 70].

def removeRange(arr, start, end):
    arr = arr[:start] + arr[end+1:]
    return arr

# Test Cases
print(removeRange([20,30,40,50,60,70], 2, 4))
