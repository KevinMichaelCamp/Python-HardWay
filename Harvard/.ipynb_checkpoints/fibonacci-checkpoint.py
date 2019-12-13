def fibonacci(n):
    a = b = 1
    for i in range(n):
        print(b)
        yield a
        a, b = b, a +b


print(sum(fibonacci(100)))
