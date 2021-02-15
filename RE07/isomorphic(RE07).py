def isomorphic(astring1, astring2):
    dic = {}
    result1 = ""
    tup = []
    for i, value in enumerate(astring2):
        for _, valor in enumerate(astring1):
            if astring2.count(value) == 1 or i == astring2.index(value):
                if valor not in dic:
                    dic[valor] = value
                    tup.append((valor, value), )
                    break
    for i in astring1:
        if i in dic:
            result1 += dic[i]
    if result1 == astring2:
        return "'{}' and '{}' are isomorphic because we can map: {}" .format(astring1, astring2, tup)
    else:
        return "'{}' and '{}' are not isomorphic" .format(astring1, astring2)


print(isomorphic('paper', 'title'))
