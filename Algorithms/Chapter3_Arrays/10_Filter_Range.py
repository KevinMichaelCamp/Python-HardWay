# Given an array and values min and max, retain only the array values between min and max.

def filterRange(arr, min, max):
    i = 0
    while i < len(arr):
        # print(i, "WHILE loop", arr)
        if arr[i] < min or arr[i] > max:
            arr = arr[:i] + arr[i+1:]
            # print(i, "IF loop", arr)
            i -= 1
        i += 1

    return arr

# Test Cases
print(filterRange([1,2,3,4,5,6,7,8,9], 3, 8))

# Using built-ins
def filterRange(arr, min, max):
    i = 0
    while i < len(arr):
        if arr[i] < min or arr[i] > max:
            del arr[i]
            i -= 1
        i += 1

    return arr

# Test Cases
print(filterRange([1,2,3,4,5,6,7,8,9], 3, 8))
