def manipulator(l, cmds):
    result = ""
    for i in cmds:
        a = i.split()
        if len(a) != 1:
            for _ in a:
                if _ == "insert":
                    l.insert(int(a[1]), int(a[2]))
                elif _ == "remove":
                    l.remove(int(a[1]))
                elif _ == "append":
                    l.append(int(a[1]))
        elif len(a) == 1:
            if i == "pop":
                l.pop()
            elif i == "reverse":
                l.reverse()
            elif i == "sort":
                l.sort()
            elif i == "print":
                result += str(l) + " "
    return result.rstrip(" ")
