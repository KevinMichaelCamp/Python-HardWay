# You are passed an array containing strings. Working within the same
# array, replace each string with a number - the length of the string
# at previous array index - and return the array.

def previousLengths(arr):
    for i in range(len(arr)-1, 0, -1):
        arr[i] = len(arr[i-1])

    return arr

# Test Cases
print(previousLengths(["Hello", "my", "name", "is", "Kevin"]))
