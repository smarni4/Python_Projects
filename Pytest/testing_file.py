def fibonacci_series(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


for number in fibonacci_series(10):
    print(number)
