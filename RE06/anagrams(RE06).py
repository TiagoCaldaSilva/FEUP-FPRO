def anagrams(alist):
    if not alist:
        return []
    b = []
    d = []
    ind = 0
    res = []

    result = []
    words_index = 0
    for i in alist:
        c = i.split()
        for j in c:
            x = j.lower()
            for t in x:
                d += t
            d.sort()
        b += [d, ]
        d = []
    for i in b[:(len(b) - 1)]:
        inde = ind + 1
        if b[:ind].count(i) == 0:
            if b[inde:].count(i) >= 1:
                copy = b.copy()
                temp = b.copy()
                ban = 0
                n = []
                for j in temp:
                    if j == i:
                        copy.remove(j)
                        n += [ban, ]
                    ban += 1
                num = []
                for nu in n:
                    num.append((alist[nu], nu))
                r = []
                re = []
                for nu in num:
                    r.append((nu[0].lower(), nu[1]))
                r = sorted(r, key=lambda v: (v[0]))
                for nu in r:
                    ti = int(nu[1])
                    re += [alist[ti]]
                res.append(re)
            else:
                res.append([alist[ind], ])
        ind += 1
    if b.count(b[len(b) - 1]) == 1:
        res.append([alist[len(b) - 1], ])
    for _ in res:
        final = []
        for i in _:
            final.append(i.lower())
        result.append((final, words_index))
        words_index += 1
    result = sorted(result, key=lambda v: (v[0]))
    resuu = []
    for j in result:
        ti = int(j[1])
        resuu.append(res[ti])
    return resuu
