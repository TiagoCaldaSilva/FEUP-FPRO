import urllib.request


def longest_word(url):
    response = urllib.request.urlopen("https://raw.githubusercontent.com/fpro-feup/public/master/assigns/13/words")
    dict = response.read().decode().split()
    dict = set(dict)
    response = urllib.request.urlopen(url)
    
    word = response.read().decode().split()
    result = []
    for i in word:
        if type(i) == str and (set([i.rstrip('\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+-./:;<=>?@[\\]^_`{|}~\x7f\x80,'),]) & dict) != set():
            result.append(i.rstrip('\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+-./:;<=>?@[\\]^_`{|}~\x7f\x80,'))
    max = 0
    r = []
    for i in result:
        if len(i) > max:
            r = [i,]
            max = len(i)
        elif len(i) == max:
            r.append(i)
    r.sort()
    return r[0]

print(longest_word("https://www.record.pt/"))
#print(longest_word('https://web.fe.up.pt/~jlopes/doku.php/teach/fpro/sheet'))
#print(longest_word('https://en.wikipedia.org/w/index.php?title=Monty_Python'))
#print(longest_word('https://en.wikipedia.org/w/index.php?title=University_of_Porto'))
#print(longest_word('https://www.w3schools.com/python/python_intro.asp'))