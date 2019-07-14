# Create a function messyMath(num) that will return the following sum: add all integers from 0 up to the given num, except for the following special cases of count value: 1. if current count (not num) is evenly divisible by 3, don;t add to sum, skip to next count; 2. otherwise, if current count is divisible by 7, include it twice in the sum instead of once; 3. Regardless of the other 2 rules, if current count is exactly 1/3 of num, return -1 immediately. For example: if given number is 4, return 7.  If given number is 8, return 34. If given number is 15, return -1

def messyMath(num):
    count = 0
    total = 0

    for i in range(num + 1):
        if count == num/3:
            return -1
        elif count % 3 == 0:
            count += 1
        elif count % 7 == 0:
            count += 1
            total += (i * 2)
        else:
            count += 1
            total += i

    return total

# Test cases
print(messyMath(4))
print(messyMath(8))
print(messyMath(15))
