# Given an array, return the sum of the first value in the array, plus
# the array's length. What happens if the array's first value is not
# a number, but a string (like "what?") or a boolean (like False)?

def firstPlusLength(arr):
    return(arr[0] + len(arr))

print(firstPlusLength([2,4,6,8]))

#print(firstPlusLength(["what","the","heck"]))

print(firstPlusLength([False, True, False]))    
