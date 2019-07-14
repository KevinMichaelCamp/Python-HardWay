# Implement function sigma(num) that given a number, returns the sum of all positive integers up to number (inclusive). Example: sigma(3) = 6 or (1+2+3); sigma(5) = 15 or (1+2+3+4+5)

def sigma(num):
    sigma = 0

    for i in range(num, -1, -1):
        sigma += i

    return sigma

# Test Cases
print(sigma(3))

print(sigma(5))
