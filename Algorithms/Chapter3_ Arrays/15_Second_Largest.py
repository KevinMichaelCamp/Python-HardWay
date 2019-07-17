# Returns the second-largest element of an array. Given [42,1,4, math.pi, 7], return 7. If the array is too short, return None.

import math

def secondLargest(arr):
    if len(arr) < 2:
        return None
    else:
        arr.sort()
        return arr[-2]

# Test Cases
print(secondLargest([42,1,4, math.pi, 7]))
print(secondLargest([5]))
