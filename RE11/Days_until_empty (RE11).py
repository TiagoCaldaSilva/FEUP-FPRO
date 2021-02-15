def days_until_empty(c, l):
    c_in = int(c)
    i = 0
    while c > 0:
        if c + l >= c_in:
            c = int(c_in)
        else:
            c = c + l
        c -= i
        if c != 0:
            i += 1
    return i

print(days_until_empty(10,0))