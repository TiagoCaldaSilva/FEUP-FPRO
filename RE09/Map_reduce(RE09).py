from functools import reduce
def map_reduce(n1, n2):return reduce(lambda x, y: x * y if x * y < 50 else x + y, [x * x for x in range(n1, n2) if x % 2 != 0])
