def find_me(f, limits):
    i = 0
    t = 0
    while True:
        a = range(limits[0], limits[1])
        m = (limits[0] + limits[1]) // 2
        if list(map(f, [m, ]))[0] == 0:
            t = 1
            return i
        else:
            if list(map(f, [m, ]))[0] == -1:
                limits = (limits[0], m)
            elif list(map(f, [m, ]))[0] == 1:
                limits = (m, limits[1])
        i += 1


print(find_me(lambda n: -1 if n > 31 else 1 if n < 31 else 0, (0, 100)))