# Create a function to generate Fibonacci numbers. Each number is the sum of the previous two, starting with the values 0 and 1. Your function should accept one argument, an index into the sequence (where 0 corresponds to the initial value 0, 4 corresponds to the value four later, etc.) Example: fibonacci(0) = 0, fibonacci(1) = 1, fibonacci(2) = 1, fibonacci(3) = 2, fibonacci(4) = 3, fibonacci(5) = 5, fibonacci(6) = 8, fibonacci(7) = 13, etc.

def fibonacci(index):
    fibSequence = [0,1]

    for i in range(2, index + 1):
        fibSequence.append(fibSequence[i-1] + fibSequence[i-2])

    return fibSequence[-1]

print(fibonacci(7))

# Print Fibonacci sequence for 50 places
def fibonacciSequence():
    fibSequence = [0,1]

    for i in range(2, 51):
        fibSequence.append(fibSequence[i-1] + fibSequence[i-2])

    return fibSequence

print(fibonacciSequence())
