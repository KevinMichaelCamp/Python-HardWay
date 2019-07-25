# Accept a string and return the number of non-space characters found in the string. For example, given, "Honey pie, you are driving me crazy" return 29 (not 35).

def countNonSpaces(string):
    count = 0

    for char in string:
        if char != " ":
            count += 1

    return count

# Test Cases
print(countNonSpaces("Honey pie, you are driving me crazy"))
