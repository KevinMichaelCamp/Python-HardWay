#Print all integer multiples of 5, from 512 to 4096. Afterward, print how many there were.

#Method 1
count = 0
for i in range(512, 4097):
    if i % 5 == 0:
        print(i)
        count += 1

print('Total multiples of five - ' + str(count))

#Method 2
count = 0
for i in range(515, 4097, 5):
    print(i)
    count += 1

print('Total multiples of five - ' + str(count))
