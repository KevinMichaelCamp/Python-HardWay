# Create a function that accepts an array. Every time the array has three odd values in a row, print "That's odd!". Every time the array has three evens in a row print "Even more so!"

def evensOdds(arr):
    for i in range(len(arr)-2):
        if arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
            print("That's odd!")
        elif arr[i] % 2 == 0 and arr[i+1] % 2 == 0 and arr[i+2] % 2 == 0:
            print("Even more so!")

# Test Cases
print("Test Case 1")
evensOdds([1,1,1,2,3,4,5])
print('\n')

print("Test Case 2")
evensOdds([2,2,2,3,4,5,6])
print('\n')

print("Test Case 3")
evensOdds([1,1,1,2,2,2])
print('\n')

print("Test Case 4")
evensOdds([1,2,3,4,5])
