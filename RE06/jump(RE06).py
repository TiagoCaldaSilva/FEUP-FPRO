def jump(l):
    count = 0
    value = l[0]
    while value != -1:
        value = l[value]
        count += 1
    return count


print(jump([8, 11, 6, 2, 7, 1, 4, -1, 10, -1, 3, 9]))
