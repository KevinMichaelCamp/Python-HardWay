# You are given an array of numbers. After every tenth element, add an additional element containing the sum of those ten values. If the array does not end aligned evenly with ten elements, add one last sum that includes those last elements not yet included in previous sums. Given array [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2], change it to [1,2,1,2,1,2,1,2,1,2,15,1,2,1,2,6]

def intermediateSums(arr):
    loops, remainder = divmod(len(arr), 10)
    intermediate_sum = 0
    j = 0

    while j < loops:
        for i in range(10+j):
            intermediate_sum += arr[i]
        arr.insert(10, intermediate_sum)
        j += 1


    remainder_sum = sum(arr[(loops*10+loops):])
    arr.insert((loops*10+loops+remainder), remainder_sum)

    return arr

# Test Cases
print(intermediateSums([1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2]))
