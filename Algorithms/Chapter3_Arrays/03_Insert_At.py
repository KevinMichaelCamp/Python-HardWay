# Given an array, an index, and an additional value, insert the value into the array at the given index. No built-ins e.g.(.insert(index, value))

def insertAt(arr, index, value):
    arr = arr[:index] + [value] + arr[index:]
    return arr

# Test Cases
print(insertAt([1,2,3,5,6], 3, 4))
