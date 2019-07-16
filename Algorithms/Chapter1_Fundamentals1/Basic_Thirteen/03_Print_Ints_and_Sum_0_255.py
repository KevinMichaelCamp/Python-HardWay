# Print integers from 0 to 255, and with each integer print the sum so far.

sum = 0

for num in range(256):
    sum += num
    print(num, '\n', "Sum:", sum)
