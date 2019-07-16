# Given an array with heights of consecutive buildings, starting closest to you and extending away. Array [-1,7,3] would represent 3 buildings: first is out of view below street level, behind it is second at 7 stories high, third is at 3 stories high (hidden by second building). Return array with heights of buildings that are visible, in order. Given [-1,1,1,7,3], return [1,7]. Given [0,4] return [4].

def skylineHeights(arr):
    i = 0
    max = arr[0]

    while i < len(arr):
        print("i=", i, "arr=", arr)
        if arr[i] <= 0:
            del arr[i]
            i -= 1
        elif arr[i] <= max:
            del arr[i]
            i -= 1
        elif arr[i] > max:
            max = arr[i]
        i += 1

    return arr

# Test Cases
print(skylineHeights([-1,1,1,7,3]))
print(skylineHeights([0,4]))
