#Using FOR, print multiples of 3 from -300 to 0. Skip -3 and -6

#Method 1
for i in range(-300, 1):
    if i == -3 or i == -6:
        continue
    elif i % 3 == 0:
        print(i)

#Method 2
for i in range(-300, 1, 3):
    if i == -3 or i == -6:
        continue
    else:
        print(i)
