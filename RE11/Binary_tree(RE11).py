def binary_tree(key, value):
    if value[0] < key:
        return binary_tree(key, value[len(value) -1]())
    elif value[0] > key:
        return binary_tree(key, value[2]())
    elif value[0] == key:
        return value[1]
    


print(binary_tree('hummer', ('aptitudes', 495, lambda: 1/0, lambda: ('roadblock', 25, lambda: ('paramedic', 211, lambda: ('bizets', 115, lambda: 1/0, lambda: ('modernizes', 848, lambda: ('lees', 937, lambda: ('gusty', 472, lambda: 1/0, lambda: ('haggles', 648, lambda: 1/0, lambda: ('jaclyns', 170, lambda: ('implication', 297, lambda: ('hummer', 561, lambda: 1/0, lambda: 1/0), lambda: 1/0), lambda: 1/0))), lambda: 1/0), lambda: 1/0)), lambda: 1/0), lambda: 1/0))))
