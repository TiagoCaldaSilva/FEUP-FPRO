def local_minima(alist, n):
    result = []
    n = n // 2
    for i, value in enumerate(alist):
        if i == 0:
            a = []
            c = 0
            while c <= n:
                a.append((alist[c], c))
                c += 1
            if min(a) == (value, i):
                result.append((value, i))
        elif n <= i <= ((len(alist) - 1) - n):
            a = []
            c = 0
            cons = 0
            while c <= (2 * n):
                a.append((alist[(i - n + c)], (i - n + c)))
                c += 1
            for _ in range(n):
                if a[_] in result:
                    cons = 1
            if cons == 0:
                if min(a[n:]) == (value, i):
                    result.append((value, i))
        elif n > i > 0:
            a = []
            c = int(i)
            cons = 0
            while c > 0:
                a.append((alist[i - c], (i - c)))
                c -= 1
            while c <= n:
                a.append((alist[i + c], (i + c)))
                c += 1
            for _ in range(n):
                if a[_] in result:
                    cons = 1
            if cons == 0 and min(a) == (value, i):
                result.append((value, i))
        elif i > ((len(alist) - 1) - n):
            a = []
            cons = 0
            c = int(i)
            while c < len(alist):
                a.append((alist[c], c))
                c += 1
            c = 1
            while c <= n:
                a.append(((i - c), (i - c)))
                c += 1
            for _ in range(n):
                if a[_] in result:
                    cons = 1
            if cons == 0 and min(a) == (value, i):
                result.append((value, i))
    return result

