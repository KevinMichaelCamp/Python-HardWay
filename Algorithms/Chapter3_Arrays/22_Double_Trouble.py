# Create a function that changes a given array to list each original element twice, retaining original order. Convert [4, "Ulysses", 42, False] to [4, 4, "Ulysses", "Ulysses", 42, 42, False, False].

def doubleElements(arr):
    double_length = 2 * len(arr)
    i = 0

    while i < double_length:
        print("i=", i, "arr=", arr)
        arr.insert(i+1, arr[i])
        i += 2
    return arr

# Test Cases
print(doubleElements([4, "Ulysses", 42, False]))
