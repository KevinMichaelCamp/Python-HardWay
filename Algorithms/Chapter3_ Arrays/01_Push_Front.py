# Given array and an additional value, insert this value at the beginning of the array. No built-in methods (.insert(index, value))

def pushFront(arr, num):
    arr[:0] = [num]
    return arr

# Test Cases
print(pushFront([1,2,3,4,5], 7))
