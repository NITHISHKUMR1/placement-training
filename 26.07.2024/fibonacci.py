def fibonacci(n):
    if n <= 1:
        return n
    x,y= 0, 1
    for _ in range(n - 1):
        x, y = x, x + y
    return x

print(fibonacci(10))