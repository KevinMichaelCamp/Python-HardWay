# Print all odd integers 1-255

# Method 1
for num in range(1, 256):
    if num % 2 != 0:
        print(num)

# Method 2
for num in range(1, 256, 2):
    print(num)
