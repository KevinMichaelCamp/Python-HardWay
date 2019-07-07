# Sort a list using selection sort. Loop through array starting with index 0, find minimum value, swap to beginning of array and continue looping through array

def selectionSort(arr):

    print("Original Array - ", arr)
    for i in range(len(arr)):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
        print("Iteration " + str(i+1), arr)
        print('\n', '*'*50, '\n')

    return arr


# Test Cases
print("Test Case 1")
arr1 = [1,5,3,2,0,8]
print("Sorted Array - ", selectionSort(arr1))

print("Test Case 2")
arr2 = [1,-53,32,-25,0,48]
print("Sorted Array - ", selectionSort(arr2))
