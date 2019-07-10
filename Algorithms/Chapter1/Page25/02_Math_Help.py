# You are given two numbers -  coefficients M and B in the equation Y = MX + B. Build a function to return the X-intercept.

def xIntercept(M, B):
    xIntercept = (-B/M)
    return xIntercept

print(xIntercept(2, 3))
