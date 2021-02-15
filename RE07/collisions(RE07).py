def collisions(alist):
    dic = {}
    for i in alist:
        tot = 0
        while i >= 1:
            tot += (i % 10)
            i //= 10
        if (tot % 8) in dic:
            dic[tot % 8] += 1
        else:
            dic[tot % 8] = 1
    return dic


print(collisions([1, 789, 100, 9807, 1208, 92, 101]))