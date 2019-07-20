# Given array, sort and remove duplicate values. Try without nested loops

def removeDuplicates(arr):
    arr.sort()
    i = 0

    while i < len(arr)-1:
        if arr[i] == arr[i+1]:
            arr = arr[:i] + arr[i+1:]
            i -= 1
        i += 1

    return arr

# Test Cases
print(removeDuplicates([1,2,3,3,4,5,5,6,7]))
print(removeDuplicates([1,2,3,3,3,4,5,5,6,7]))

# Without nested loops
def removeDuplicates(arr):
    return list(dict.fromkeys(arr))

print(removeDuplicates([1,2,3,3,4,5,5,6,7]))
