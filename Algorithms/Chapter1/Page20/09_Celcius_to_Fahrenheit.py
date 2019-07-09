# Create celciusToFahrenheit(cDegrees) that accepts number of degrees
# Celcius and returns the equivalent temperature expressed in degrees
# Fahrenheit.

# Find where Celcius and Fahrenheit are equivalent. Start at Celcius
# 200 degrees and go downward

def celciusToFahrenheit(cDegrees):
    fDegrees = (9/5) * cDegrees + 32
    return fDegrees

# Test Cases
print(celciusToFahrenheit(0))

print(celciusToFahrenheit(100))


for c in range(200, -200, -1):
    if c == (9/5) * c + 32:
        print(c)


