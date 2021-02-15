import random


def bulls_cows(seed):
    def closure(guess):
        random.seed(seed)
        num = str(random.randint(0000, 9999))
        b = 0
        c = 0
        for i, v in enumerate((str(guess))):
            if v == num[i]:
                c += 1
                num = num[:i] + "t" + num[i + 1:]
                guess = str(guess)[:i] + "t" + str(guess)[i + 1:]
        for i, v in enumerate((str(guess))):
            if num.count(v) != 0 and num[i] != v:
                b += 1
                num = num[:num.index(v)] + "t" + num[num.index(v) + 1:]
                guess = str(guess)[:i] + "t" + str(guess)[i + 1:]
        return (c, b)
    return closure


print(bulls_cows(123)(7890))