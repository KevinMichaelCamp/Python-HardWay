# Stan learned something today: that directly decrementing an array's .length immediately shortens it by that amount. Given array arr and number x, remove all except the last x elements, and return arr (changed and shorter). Given ([2,4,6,8,10], 3), change the given array to [6,8,10] and return it.

def shortenArray(arr, x):
    arr = arr[-x:]
    return arr

print(shortenArray([2,4,6,8,10], 3))
