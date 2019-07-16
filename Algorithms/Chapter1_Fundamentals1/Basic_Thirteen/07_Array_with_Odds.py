# Create an array with all odd integers between 1 and 255 (inclusive).

# Method 1
oddArray = []
for i in range(1, 256):
    if i % 2 != 0:
        oddArray.append(i)

print(oddArray)

# Method 2
oddArray = []
for i in range(1, 256, 2):
    oddArray.append(i)

print(oddArray)
