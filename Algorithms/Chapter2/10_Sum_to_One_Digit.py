## Sexy algorithm solution

# Implement digitSum(num) that sums a given integer's digits repeatedly until the sum is only one digit. Return that one-digit result. Example: sumToOne(928) return 1, because 9+2+8=19, then 1+9=10, then 1+0=1.

def digitSum(num):
    if (num == 0):
        return 0
    if (num % 9 == 0):
        return 9
    else:
        return (num % 9)

print(digitSum(928))
print(digitSum(31654))
