def re_letter_rev(ch, astr):
    c = astr.split(ch)
    print(c)
    b = ""
    for i in c:
        b += i
    return b[::-1]


print(re_letter_rev('O', 'nothing'))
