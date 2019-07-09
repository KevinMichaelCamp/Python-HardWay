# Given array, add 1 to odd elements([1], [3], etc.), print all values and return array

def incrementSeconds(arr):
    for i in range(len(arr)):
        if i % 2 != 0:
            arr[i] += 1
        print(arr[i])
    return arr

# Test Cases
print(incrementSeconds([1,2,3,4,5,6,7]))
