# Given a string array and value(length), remove any strings shorter than length from the array.

def removeShorterStrings(array, length):
    for string in array:
        if len(string) < length:
            array.remove(string)
    return array


# Test Cases
print(removeShorterStrings(["Hello", "my", "name,", "is", "Kevin"], 3))
