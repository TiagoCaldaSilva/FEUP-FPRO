def logic(s, operations):
    for k, v in operations.items():
        if k == "and":
            s = (s & v)
        if k == "not":
            s = (v - s)
        if k == "xor":
            s = v ^ s
        if k == "or":
            s = v | s
    return s


print(logic({1, 2, 3, 4}, {'and': {3, 4, 5, 6}}))