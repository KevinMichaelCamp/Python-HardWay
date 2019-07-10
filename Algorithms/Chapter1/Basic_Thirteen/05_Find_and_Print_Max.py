# Given an array, find and print its largest element.

def findPrintMax(arr):
    max = arr[0]

    for i in arr:
        if i > max:
            max = i
    return max

# Test Cases
print(findPrintMax([1,2,3,4,5,6]))
print(findPrintMax(["Hi", "my", "name", "is", "Kevin"]))
