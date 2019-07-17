# Create function shuffle(arr), to efficiently shufffle an array's values

import random

def shuffle(arr):
    random.shuffle(arr)
    return arr

# Test Cases
print(shuffle([1,2,3,4,5,6,7,8,9]))
