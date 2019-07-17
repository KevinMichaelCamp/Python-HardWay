# Return the element that is N-from array's end. Given ([5,2,3,6,4,9,7], 3) return 4. If the array is too short, return None.

def nthToLast(arr, n):
    if len(arr) < n:
        return None
    else:
        return arr[-n]

# Test Cases
print(nthToLast([5,2,3,6,4,9,7], 3))
print(nthToLast([5,2,3,5], 6))
