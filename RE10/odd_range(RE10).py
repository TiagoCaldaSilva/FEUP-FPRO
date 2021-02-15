#def odd_range(start, stop, step):
#    a = filter(lambda x: x % 2 == 1, [x for x in range(start, stop)])
#    return filter(lambda x: x[1] - x[x[0] - 1] >= step, enumerate(a))

def odd_range(start, stop, step):
    a = [x for x in range(start, stop) if x % 2 == 1]
    i =  0
    while i <= len(a):
        yield a[i]
        i += step


print(odd_range(0, 20, 2))