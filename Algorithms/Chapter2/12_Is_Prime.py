# Return whether a given number is prime. Prime numbers are only divisible by themselves and 1. Many highly optimized solutions exists, create one that is easy to understand annd debug.

def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Test Cases
print("Should return False:")
print(isPrime(4))
print(isPrime(6))
print(isPrime(8))
print(isPrime(9))
print(isPrime(10))
print(isPrime(12))
print(isPrime(14))
print(isPrime(15))
print(isPrime(16))
print(isPrime(18))
print(isPrime(20))
print('\n', "Should return True")
print(isPrime(2))
print(isPrime(3))
print(isPrime(5))
print(isPrime(7))
print(isPrime(11))
print(isPrime(13))
print(isPrime(17))
print(isPrime(19))
print(isPrime(23))
print(isPrime(29))
