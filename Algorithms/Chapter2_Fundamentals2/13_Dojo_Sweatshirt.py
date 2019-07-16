# Sweatshirts cost $20 (including tax), with a 9% discount if you buy 2, a 19% discount if you buy 3, and a 35% discount if you buy four or more. Round to nearest dollar. Build function sweatshirtPricing(num) that given a number of sweatshirts, returns the cost.

def sweatshirtPricing(num):
    rate = 20

    if num == 1:
        discount = 0
    elif num == 2:
        discount = (rate * num) * .09
    elif num == 3:
        discount = (rate * num) * .19
    elif num >= 4:
        discount = (rate * num) * .35
    price = rate * num - discount

    return round(price)

# Test Cases
print(sweatshirtPricing(1))
print(sweatshirtPricing(2))
print(sweatshirtPricing(3))
print(sweatshirtPricing(4))
print(sweatshirtPricing(5))
