def calculator(expr):
    if type(expr[0]) == tuple:
        t1 = calculator(expr[0])
    else:
        t1 = expr[0]
    if type(expr[2]) == tuple:
        t2 = calculator(expr[2])
    else:
        t2 = expr[2]
    if expr[1] == "+":
        return t1 + t2
    elif expr[1] == "*":
        return t1 * t2
    elif expr[1] == "-":
        return t1 - t2
