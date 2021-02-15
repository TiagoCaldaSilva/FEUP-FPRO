def raise_exception(alist, value):
    r = []
    for i in alist:
        if i <= value:
            my_error = ValueError('{} is not greater than {}'.format(i, value),)
            r.append(my_error)
    return r
print(raise_exception([1, -2, 3, 0], 3))