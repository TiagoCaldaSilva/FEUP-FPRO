def bisect(f, n):
    lower = 0
    upper = 1
    m = 0
    i = 0
    while i != n:
        i += 1
        m = (upper + lower) / 2
        if (f(m) < 0 and f(lower) < 0) or (f(m) > 0 and f(lower) > 0):
            lower = m
        else:
            upper = m
    return round(m, 5)
