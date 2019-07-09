# Given array, swap first and last, third and third-to-last, etc. Input [True, 42, "Ada", 2, "pizza"] becomes ["pizza", 42, "Ada", 2, True]. Change [1,2,3,4,5,6] to [6,2,4,3,5,1]

def swapTowardCenter(arr):
    for i in range(len(arr)//2):
        if i % 2 == 0:
            arr[i], arr[-(i+1)] = arr[-(i+1)], arr[i]
    return arr

# Test Cases
print("Test Case 1")
print(swapTowardCenter([True, 42, "Ada", 2, "pizza"]))
print('\n')

print("Test Case 2")
print(swapTowardCenter([1,2,3,4,5,6]))
