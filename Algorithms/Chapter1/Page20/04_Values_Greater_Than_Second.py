# For [1,3,5,7,9,13], print values that are greater than its second
# value. Return how many values this is.

arr = [1,3,5,7,9,13]
count = 0

for i in arr:
    if i > arr[1]:
        count += 1
        print(i)

print("There are " + str(count) + " values greater than the second")
