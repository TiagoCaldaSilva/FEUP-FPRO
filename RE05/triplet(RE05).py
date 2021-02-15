def triple(atuple):
    for i, a in enumerate(atuple[:len(atuple) - 2]):
        ind = int(i)
        for b in atuple[i + 1: len(atuple) - 1]:
            ind += 1
            for c in atuple[ind + 1:]:
                if int(a) + int(b) + int(c) == 0:
                    return (a, b, c)
    return ()


def triplet(atuple):
    ind = 0
    inde = ind + 2
    for i in atuple[:(len(atuple) - 2)]:
        ind += 1
        for ii in atuple[ind:(len(atuple) - 1)]:
            if (inde in list(range(2, len(atuple)))) is False:
                inde = ind + 1
            for iii in atuple[(inde):]:
                if int(i) + int(ii) + int(iii) == 0:
                    return (i, ii, iii)
            inde += 1
    return ()

