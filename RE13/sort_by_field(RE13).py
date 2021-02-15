def sort_by_field(filename, field):
    with open(filename, "r") as myfile:
        a = myfile.read().splitlines()
    a = [x.split(",") for x in a]
    first = a[0]
    x = first.index(field)
    r = sorted(a[1:], key=lambda t:t[x])
    r = "\n".join([",".join(x) for x in r])
    return ",".join(first) + "\n" + r