# Create a function that accepts an array. If value at [0] is greater
# than array's length, print "Too big!"; if value at [0] is less than
# array's length, print "Too small!"; otherwise print "Just right!".

def fitFirstValue(arr):
    if arr[0] > len(arr):
        print("Too big!")
    elif arr[0] < len(arr):
        print("Too small!")
    else:
        print("Just right!")

# Test Cases
fitFirstValue([1,2,3,4,5])

fitFirstValue([7,1,2,3,4])

fitFirstValue([5,2,3,6,7])
