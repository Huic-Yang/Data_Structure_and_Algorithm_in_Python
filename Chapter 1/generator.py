def factor(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k


def fibonacci():
    f = 1
    g = 0
    while True:
        yield g
        f, g = g, g + f


def my_abs(x):
    return x if x > 0 else -x
