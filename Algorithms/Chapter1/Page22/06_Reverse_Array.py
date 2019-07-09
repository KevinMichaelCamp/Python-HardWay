# Given array, write a function that reverses values, in-place. Example: reverse([3,1,6,4,2]) returns the same array, containing [2,4,6,1,3].

# Without built-in methods
def reverse(arr):
    for i in range(len(arr)//2):
        arr[i], arr[-(i+1)] = arr[-(i+1)], arr[i]
    return arr

print(reverse([3,1,6,4,2]))

# Built in list.reverse()
arr = [3,1,6,4,2]
arr.reverse()
print(arr)
