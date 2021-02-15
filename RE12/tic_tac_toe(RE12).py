def tic_tac_toe(board, player):
    A = []
    B = []
    C = []
    for i, valor in enumerate(board):
        if 0 <= i < 3:
            A.append(valor)
        elif 4 <= i < 7:
            B.append(valor)
        elif 8 <= i:
            C.append(valor)
    D1 = [A[0], B[1], C[2]]
    D2 = [A[2], B[1], C[0]]
    V0 = [A[0], B[0], C[0]]
    V1 = [A[1], B[1], C[1]]
    V2 = [A[2], B[2], C[2]]
    d = ["A", "B", "C"]
    if A.count(player) == 2 and A.count(" ") == 1:
        return "A" + str(A.index(" ") + 1)
    elif B.count(player) == 2 and B.count(" ") == 1:
        return "B" + str(B.index(" ") + 1)
    elif C.count(player) == 2 and C.count(" ") == 1:
        return "C" + str(C.index(" ") + 1)
    elif D1.count(player) == 2 and D1.count(" ") == 1:
        return d[D1.index(" ")] + str(D1.index(" ") + 1)
    elif D2.count(player) == 2 and D2.count(" ") == 1:
        return d[D2.index(" ")] + str(3 - (D2.index(" ") + 1))
    elif V0.count(player) == 2 and V0.count(" ") == 1:
        return d[V0.index(" ")] + "1"
    elif V1.count(player) == 2 and V1.count(" ") == 1:
        return d[V1.index(" ")] + "2"
    elif V2.count(player) == 2 and V2.count(" ") == 1:
        return d[V2.index(" ")] + "3"