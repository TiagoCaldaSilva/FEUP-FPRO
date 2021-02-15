def palindrome(astring):
    count = 0
    if len(astring) == 1:
        return "The string {} contains {} palindrome substrings." .format(count, astring)
    else:
        #começar por vr 2 a duas se são iguais
        ind = 0
        for i in astring[:len(astring) -1]:
            if i == astring[(ind + 1)]:
                count += 1
            ind += 1
        #ver 3 a 3
        ind = 1
        for i in astring[1:(len(astring) - 1)]:
            b = astring[(ind - 1): (ind + 2)]
            if b == b[::-1] and i != astring[ind + 1]:
                count += 1
            ind += 1
        #ver com 4
        if len(astring) >= 4:
            ind = 2
            for i in astring[2: (len(astring) - 2)]:
                b = astring[(ind - 2): (ind + 2)]
                if b == b[::-1] and i != astring[(ind + 1)]:
                    count += 1
                ind += 1
        #ver a própria string
        if len(astring) != 2 and len(astring) != 3 and len(astring) != 4:
            if astring == astring[::-1]:
                count += 1
        return "The string {} contains {} palindrome substrings." .format(count, astring)
