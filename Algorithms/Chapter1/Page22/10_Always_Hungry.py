# Create a function that accepts an array, and print "yummy" each time one of the values is equal to "food". If no array elements are "food" then print "I'm hungry" once.

def alwaysHungry(arr):
    if "food" not in arr:
        print("I'm hungry")
        return
    for item in arr:
        if item == "food":
            print("yummy")

# Test Cases
alwaysHungry(["food", "food", "notfood"])
alwaysHungry([1,2,3])
