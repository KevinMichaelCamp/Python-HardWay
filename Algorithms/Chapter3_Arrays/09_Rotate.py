# Implement rotateArr(arr, shiftBy) that accepts array and an offset. Shift arr's values to the right by that amount. 'Wrap around' any values that shift off the array's end to the other side, so that no data is lost. Operate in place. Given ([1,2,3], 1) return [3,1,2].

def rotateArr(arr, shiftBy):
    if shiftBy > 0:
        arr = arr[-shiftBy:] + arr[:shiftBy+1]
        return arr
    else:
        arr = arr[-shiftBy:] + arr[:-shiftBy]
        return arr

# Test Cases
print(rotateArr([1,2,3], 1))
print(rotateArr([1,2,3], -1))
print(rotateArr([1,2,3], 0))
print(rotateArr([1,2,3,4,5,6,7,8,9], 4))
print(rotateArr([1,2,3,4,5,6,7,8,9], -4))
