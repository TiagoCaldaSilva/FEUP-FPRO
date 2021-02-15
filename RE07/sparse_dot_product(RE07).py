def sparse_dot_product(dict1, dict2):
    result = 0
    if max(dict1) < max(dict2):
        a = max(dict2)
    else:
        a = max(dict1)
    vetor1 = []
    vetor2 = []
    for i in range(a + 1):
        if i in dict1:
            c = dict1[i]
            vetor1.append(c)
        else:
            vetor1.append(0)
        if i in dict2:
            c = dict2[i]
            vetor2.append(c)
        else:
            vetor2.append(0)
    for i, value in enumerate(vetor1):
        result += (value * vetor2[i])
    return result


print(sparse_dot_product({0: 1, 1: 1}, {2: 1, 3: 1}))