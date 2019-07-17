# Given arr and N, return the Nth largest element, where (N-1) elements are larger. Return None if needed

def nthLargest(arr, N):
    if len(arr) < N:
        return None
    else:
        arr.sort()
        return arr[-N]

# Test Cases
print(nthLargest([1,6,7,3,2,9,5,5], 4))
print(nthLargest([1,2,3,4,5,6,7,8,9], 4))
print(nthLargest([1,2,3], 4))
