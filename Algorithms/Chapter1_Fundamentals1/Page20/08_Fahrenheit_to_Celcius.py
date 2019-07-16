# Create fahrenheitToCelcius(fDegrees) that accepts a number of degrees
# in Fahrenheit, and returns the equivalent temperature as expressed in
# Celcius degrees. MATH - Fahrenheit = (9/5 * Celcius) + 32

def fahrenheitToCelcius(fDegrees):
    cDegrees = (fDegrees - 32) / (9/5)
    return cDegrees

# Test Cases
print(fahrenheitToCelcius(100))

print(fahrenheitToCelcius(32))
