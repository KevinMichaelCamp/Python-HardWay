#print multiples of six up to 60,000 using a while loop

#Method 1
i = 0

while i <= 60000:
    if i % 6 == 0:
        print(i)
    i += 1

#Method 2
i = 6

while i <= 60000:
    print(i)
    i += 6

