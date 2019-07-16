# Given array and an index into array, remove and return the array value at that index.  No built-ins e.g. (.pop(index))

def removeAt(arr, index):
    pop = arr[index]
    arr = arr[:index] + arr[(index+1):]
    return pop

# Test Cases
print(removeAt([1,2,3,4,5], 2))
