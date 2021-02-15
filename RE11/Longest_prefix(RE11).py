def longest_prefix(words):
    dict = {}
    list = []
    for i in words:
        for x, v in enumerate(i):
            if i[:x+1] in dict:
                dict[i[:x+1]] += 1
            else:
                dict[i[:x+1]] = 1
    for i in dict:
        list.append((i, dict[i]))
    list = sorted(list, key=lambda x: (x[1], len(x[0])), reverse=True)
    return list[0][0]
