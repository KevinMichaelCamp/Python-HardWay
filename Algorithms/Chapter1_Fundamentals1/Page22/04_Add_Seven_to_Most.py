# Build a function that accepts array. Return a new array with all values except the first, adding 7 to each. Do not alter the original array.

def addSevenToMost(arr):
    new_arr = []

    for i in range(1, len(arr)):
        new_arr.append(arr[i]+7)

    return new_arr

# Test Cases
print(addSevenToMost([1,2,3,-4,-5,6,7]))
