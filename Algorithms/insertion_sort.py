# Insertion Sort - Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time.

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


# Test Cases
print("Test Case 1")
arr1 = [6,5,3,1,8,7,2,4]
print(insertionSort(arr1))
print('*'*100, '\n')

print("Test Case 2")
arr1 = [4,3,2,10,12,1,5,6]
print(insertionSort(arr1))
print('*'*100, '\n')
