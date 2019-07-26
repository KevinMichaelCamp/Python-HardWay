# Build a standalone function to remove strings of even length from a given array. For array containing ["Nope!", "Its", "Kris", "starting", "with", "K!", "(instead", "of", "Chris", "with", "C)"] return ["Nope!", "Its", " Chris"].

def removeEvenLength(arr):
    i = 0
    while i < len(arr):
        if len(arr[i]) % 2 == 0:
            arr.remove(arr[i])
            i -= 1
        i += 1

    return arr

# Test Cases
print(removeEvenLength(["Nope!", "Its", "Kris", "starting", "with", "K!", "(instead", "of", "Chris", "with", "C)"]))
