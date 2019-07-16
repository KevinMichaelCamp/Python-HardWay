# For given array, return the average

def arrayAverage(arr):
    sum = 0
    for num in arr:
        sum += num
    average = sum / len(arr)
    return average

# Test Cases
print(arrayAverage([1,2,3,4,5,6]))
