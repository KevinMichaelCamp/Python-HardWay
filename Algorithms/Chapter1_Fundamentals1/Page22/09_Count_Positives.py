# Given array of numbers, create function to replace last value with number of positive values. Example: countPositives([-1,1,1,1,]) changes array to         [-1,1,1,3] and returns it.

def countPositives(arr):
    count = 0

    for num in arr:
        if num >= 0:
            count += 1

    arr[-1] = count
    return arr

# Test Cases
print(countPositives([-1,1,1,1,]))
