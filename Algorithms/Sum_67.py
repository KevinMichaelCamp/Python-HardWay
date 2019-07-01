#Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

def sum67(nums):
  total = 0
  i = 0

  while i < len(nums):
    if nums[i] != 6:
        total += nums[i]
        i += 1
    else:
        i = (nums.index(7)+1)

  return total



print(sum67([1, 2, 2]))
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2]))
print(sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]))
