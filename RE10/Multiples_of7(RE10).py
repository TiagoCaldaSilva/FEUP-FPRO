#def multiples_of7(n):
#    return filter(lambda x: x % 7 == 0, [x for x in range(0, n)])

def multiples_of7(n):
    for i in range(21):
        if i % 7 == 0:
            yield i