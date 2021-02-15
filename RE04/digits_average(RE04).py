import math


def digits_average(n):
    while n > 9:
        num = 0
        while n >= 9:
            n1 = math.ceil((((n // 10) % 10) + (n % 10)) / 2)
            num = (num * 10) + n1
            n = n // 10
        n = num
    return(n)


print(digits_average(158))
