# Create function shuffle(arr), to efficiently shuffle an array's values. Do not use built-in functions - e.g. random.shuffle()

import random

def shuffle(arr):
    shuffled_arr = []
    new_order = random.sample(range(0, len(arr)), len(arr))
    print(new_order)
    for i in range(len(arr)):
        shuffled_arr.append(arr[new_order[i]])
    return shuffled_arr

# Test Cases
print(shuffle([1,2,3,4,5,6,7,8,9]))
