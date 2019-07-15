# Write a function factorial(num) that, given a number, returns the product (multiplication) of the all positive integers from 1 up to that number (inclusive).  Example: factorial(3) = 6 or (1*2*3); factorial(5) = 120 or (1*2*3*4*5).

def factorial(num):
    factorial = 1

    for i in range(1, num + 1):
        factorial *= i

    return factorial

# Test Cases
print(factorial(3))
print(factorial(5))
