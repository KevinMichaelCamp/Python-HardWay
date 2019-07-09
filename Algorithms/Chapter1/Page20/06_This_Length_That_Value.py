# Given two numbers, return array of length num1 with each value num2.
# Print "Jinx!" if they are the same.

def lengthValue(num1, num2):
    arr = []

    if num1 == num2:
        print("Jinx!")

    for i in range(num1):
        arr.append(num2)

    return arr

# Test Cases
print(lengthValue(7,4))

print(lengthValue(7,7))
