# Return the second-to-last element of an array. Given [42, True, 4, "Kate", 7] return "Kate". If array is too short, return null.

def secondToLast(arr):
    if len(arr) < 2:
        return None
    else:
        return arr[-2]

# Test Cases
print(secondToLast([42, True, 4, "Kate", 7]))
print(secondToLast([False]))
