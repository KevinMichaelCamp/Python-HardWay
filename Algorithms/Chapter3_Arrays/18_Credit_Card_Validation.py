# The Luhn formula is sometimes used to validate credit card numbers. Create the function validateCreditCard(digitArr) that accepts an array of digits on the card (13-19 depending on the card), and returns a boolean whether the card digits satisfy the Luhn formula, as follows: 1. Set aside the last digit - do not include in calculations(until step 5); 2. Starting from the back, mutiply the digits in odd positions(last, third-to-last, etc.) by 2; 3. If any results larger than 9, subtract 9 from them; 4. Add all numbers (not just odds) together; 5. Now add the last digit back in - the sum should be a multiple of ten.

def validateCreditCard(digitArr):
    newArr = digitArr[:-1]
    for i in range(len(newArr)-1, -1, -2):
        newArr[i] *= 2
        if newArr[i] > 9:
            newArr[i] -= 9

    total = sum(newArr) + digitArr[-1]
    if total % 10 == 0:
        return True
    else:
        return False


# Test Cases
print(validateCreditCard([4,5,3,9,6,6,6,5,1,0,6,6,4,0,5,5])) #True
print(validateCreditCard([4,5,8,3,4,4,6,8,2,5,3,1,4,1,6,2])) #False
print(validateCreditCard([3,5,3,3,5,3,9,7,2,9,0,1,8,7,5,3,4,8,4])) #True
