def regra1(s):
    return (s[0], s[1])


def regra2(s):
    return (sum(s[2]) / len(s[2]))


def sort_grade(records):
    r = sorted(records, key=regra1)
    return sorted(r, key=regra2, reverse=True)


print(sort_grade((('Tate', 'up2011111', (50, 60, 40, 30, 80, 100)), ('Jarred', 'up2012112', (60, 45, 29, 31, 42, 81)), ('Ayan', 'up2011112', (59, 61, 71, 52, 37, 0)), ('James', 'up2012111', (60, 60, 60, 70, 55)), ('Tatiana', 'up2013000', (61, 62, 63, 64, 65, 66)), ('Jasper', 'up2013010', (50, 100, 100, 90, 0, 15)), ('Jarrod', 'up2011110', (10, 30, 50, 70, 90, 100)))))


def sort_grades(records):
    return sorted(records, key=lambda t: ((100 - (sum(t[2]) / len(t[2]))), t[0], t[1]), reverse=False)


print(sort_grades((('Tate', 'up2011111', (50, 60, 40, 30, 80, 100)), ('Jarred', 'up2012112', (60, 45, 29, 31, 42, 81)), ('Ayan', 'up2011112', (59, 61, 71, 52, 37, 0)), ('James', 'up2012111', (60, 60, 60, 70, 55)), ('Tatiana', 'up2013000', (61, 62, 63, 64, 65, 66)), ('Jasper', 'up2013010', (50, 100, 100, 90, 0, 15)), ('Jarrod', 'up2011110', (10, 30, 50, 70, 90, 100)))))
