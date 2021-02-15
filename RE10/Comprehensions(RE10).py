from math import sqrt
def comprehensions(i, j):
    return [x for x in range(i, j + 1) if x % 10 == 3 or x % 10 == 8], tuple(map(lambda x: x, [round(sqrt(x), 2) for x in range(i, j + 1)])), dict([(x, chr(x)) for x in range(i, j + 1)])
