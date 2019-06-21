def computepay(h,r):
    h = float(h)
    r = float(r)

    if h <= 40:
        pay = h * r
    else:
        overtime = h - 40
        pay = (40 * r) + (overtime *(1.5*r))
    return pay

h = input("Enter Hours:")
r = input("Enter Rate:")
p = computepay(h,r)
print("Pay",p)
