# Algorithm to sort list using bubble method - (comparing pairs of numbers)

def bubble_sort(arr):
    for j in range(len(arr) - 1):
        print("j: ", j, "arr: ", arr)
        for i in range(len(arr) - 1 - j):
            print("i: ", i, "arr: ", arr)
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    print('sorted array is ', arr)


#Test Cases
print('Test Case 1', '\n', '*'*100)
arr1 = [1,5,3,2,0,8]
bubble_sort(arr1)
print('\n')

print('Test Case 2', '\n', '*'*100)
arr1 = [-22,5,32,2-56,0,52,-23,23,45,-78,55,-3]
bubble_sort(arr1)
print('\n')
