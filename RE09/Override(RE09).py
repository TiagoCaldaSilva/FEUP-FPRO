def override(l1, l2):
    c = list(map((lambda x: x[0]), l2))
    r = list(map((lambda x: x if x[0] not in c else "0"), l1))
    r = list(filter((lambda x: type(x) == tuple), r))
    return sorted((l2 + r), key=lambda x:x[0])
