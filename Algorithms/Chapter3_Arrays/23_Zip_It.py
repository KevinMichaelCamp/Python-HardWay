# Create a standalone function that accepts two arrays and combines their values sequentially into a new array, at alternating indices staring with the first array. Extra values from either array should be included afterward. Given [1,2] and [10,20,30,40], return new array containing [1,10,2,20,30,40].

def zipIt(arr1, arr2):
    new_array = []

    if len(arr1) >= len(arr2):
        longLen, shortLen = len(arr1), len(arr2)
        longArr = arr1
    else:
        longLen, shortLen = len(arr2), len(arr1)
        longArr = arr2

    for i in range(shortLen):
        new_array.append(arr1[i])
        new_array.append(arr2[i])

    for j in range(shortLen, longLen):
        new_array.append(longArr[j])

    return new_array

# Test Cases
print(zipIt([1,2], [10,20,30,40]))


# Now combine the two array's values into the first array
def zipIt2(arr1, arr2):
    for i in range(len(arr2)):
        arr1.insert(i + 1 + i, arr2[i])
        print("i=", i, "arr=", arr1)

    return arr1

#Test Cases
print(zipIt2([1,2,3,4,5,6,7,8], [10,20,30,40,50,60,70,80,90,100]))
