def roman_to_integer(astring):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i, value in enumerate(astring):
        if i != (len(astring) - 1):
            if dic[value] >= dic[astring[i + 1]]:
                total += dic[value]
            else:
                total -= dic[value]
        else:
            total += dic[value]
    return total


print(roman_to_integer())