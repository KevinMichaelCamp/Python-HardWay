# Write a function that prints the number 1, then "chick", then "boom", then "chick", then 2, then "chick", then "boom", then "chick", continuing the cycle up to and including number 12.

def twelveBarBlues():
    for i in range(12):
        print(i + 1, '\n', 'chick', '\n', 'boom', '\n', 'chick', '\n')


# Test Cases
twelveBarBlues()
