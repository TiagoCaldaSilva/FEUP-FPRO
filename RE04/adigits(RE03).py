def adigits(n1, n2, n3):
    result = ""
    a = [n1, n2, n3]
    a.sort()
    a.reverse()
    for i in a:
        result += i
    return int(result)
