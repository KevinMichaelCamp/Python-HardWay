#Add odd integers from -300,000 to 300,000 and print the sum. Is there a shortcut?

#Method 1
odd_sum = 0

for i in range(-300000, 300001):
    if i % 2 != 0:
        odd_sum += i

print(odd_sum)

#Method 2
print(sum(range(-299999, 300000, 2)))


