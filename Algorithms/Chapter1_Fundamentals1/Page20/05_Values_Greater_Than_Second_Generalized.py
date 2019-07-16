# Write a function that accepts any array, and returns a new array
# with the array values that are greater than its second value. Print
# how many values this is. What will you do if the array is only one
# element long?

def valuesGreaterThanSecond(arr):
    new_arr = []
    count = 0

    for i in arr:
        if i > arr[1]:
            new_arr.append(i)
            count += 1

    print(count)
    return new_arr

# Test Case
print(valuesGreaterThanSecond([1,2,3,4,5,6]))

