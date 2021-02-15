def brute_force(f, l):
    return list(filter(f, [x + y + z for i, x in enumerate(l) for ind, y in enumerate(l) for inde, z in enumerate(l)]))
