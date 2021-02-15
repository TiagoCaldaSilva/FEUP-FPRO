def flatten(alist):
    r = []
    for i in alist:
        if type(i) == list:
            r += flatten(i)
        else:
            r.append(i)
    return r


print(flatten(["Hello", [2, [[], False]], [True]]))