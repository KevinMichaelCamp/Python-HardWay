# Given an array, print the min, max and average values for that array.

def minMaxAverage(arr):
    min = arr[0]
    max = arr[0]
    sum = 0

    for num in arr:
        sum += num
        if num < min:
            min = num
        if num > max:
            max = num

    average = sum / len(arr)

    return min, max, average

print(minMaxAverage([1,2,3,4,5,6,7]))
