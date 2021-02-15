def move_ball(board):
    for ind, i in enumerate(board):
        if i.count("N") == 1:
            ini_pos = (ind, i.index("N"))
            d = (-1, 0)
            break
        elif i.count("E") == 1:
            ini_pos = (ind, i.index("E"))
            d = (0, 1)
            break
        elif i.count("W") == 1:
            ini_pos = (ind, i.index("W"))
            d = (0, -1)
            break
        elif i.count("S") == 1:
            ini_pos = (ind, i.index("S"))
            d = (1, 0)
            break
    result = [ini_pos, ]
    pos = ini_pos
    t = board[pos[0] + d[0]][pos[1] + d[1]]
    while t != "X":
        pos = (pos[0] + d[0], pos[1] + d[1])
        result.append(pos)
        if t == '\\' and d == (0, -1):
            d = (-1, 0)
        elif t == '\\' and d == (-1, 0):
            d = (0, -1)
        elif t == '\\' and d == (0, 1):
            d = (1, 0)
        elif t == '\\' and d == (1, 0):
            d = (0, 1)
        elif t == '/' and d == (0, 1):
            d = (-1, 0)
        elif t == '/' and d == (1, 0):
            d = (0, -1)
        elif t == '/' and d == (0, -1):
            d = (1, 0)
        elif t == '/' and d == (-1, 0):
            d = (0, 1)
        t = board[pos[0] + d[0]][pos[1] + d[1]]
    result.append((pos[0] + d[0], pos[1] + d[1]))
    return result
