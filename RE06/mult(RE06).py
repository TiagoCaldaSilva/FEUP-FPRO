def mult(M, N):
    matrix_m = {}
    matrix_n = {}
    result = []
    if len(M[0]) != len(N):
        return []
    for i, value in enumerate(M):
        for ind, valor in enumerate(value):
            matrix_m[i, ind] = valor
    for i, value in enumerate(N):
        for ind, valor in enumerate(value):
            matrix_n[i, ind] = valor
    for i in N:
        n = len(i)
    for i in range(len(M)):
        resul = []
        for c in range(n):
            r = 0
            re = 0
            for _ in range(len(N)):
                re = (matrix_m[i, _] * matrix_n[_, c])
                r += re
            resul.append(r)
        result.append(resul)
    return result
