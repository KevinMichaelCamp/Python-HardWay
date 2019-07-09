# Given array, create a function to return a new array where each value n the original has been doubled. Calling double([1,2,3]) should return [2,4,6] without changing the original array.

def double(arr):
    new_arr = []

    for i in range(len(arr)):
        new_arr.append(arr[i] * 2)
    return new_arr

# Test Cases
print(double([1,2,3]))
