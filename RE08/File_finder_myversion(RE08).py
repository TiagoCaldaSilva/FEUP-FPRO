def file_finderr(dirs, file_name):
    r = dirs[0] + "/"
    for i in dirs:
        if i == file_name:
            return r + i
        elif type(i) == list and file_finderr(i, file_name) is not None:
                return r + file_finderr(i, file_name)
            
print(file_finderr(['home', ['Documents', ['FPRO', 'lists.txt', 'recursion.pdf', 'functions'], ['Python', 'hello_world.py', 'readme.md']], ['Downloads', ['Movies', ['TV Series', 'BreakingBad.mp4', 'TheBigBangTheory.avi'], '1.avi', '22', '001.mp4']], 'tmp.txt', 'page.html'], 'Documents'))
print(file_finderr(['home', ['Documents', ['FPRO', 'lists.txt', 'recursion.pdf', 'functions'], ['Python', 'hello_world.py', 'readme.md']], ['Downloads', ['Movies', ['TV Series', 'BreakingBad.mp4', 'TheBigBangTheory.avi'], '1.avi', '22', '001.mp4']], 'tmp.txt', 'page.html'], 'page.html'))
print(file_finderr(['home', ['Documents', ['FPRO', 'lists.txt', 'recursion.pdf', 'functions'], ['Python', 'hello_world.py', 'readme.md']], ['Downloads', ['Movies', ['TV Series', 'BreakingBad.mp4', 'TheBigBangTheory.avi'], '1.avi', '22', '001.mp4']], 'tmp.txt', 'page.html'], 'hello_world.py'))
print(file_finderr(['home', ['Documents', ['FPRO', 'lists.txt', 'recursion.pdf', 'functions'], ['Python', 'hello_world.py', 'readme.md']], ['Downloads', ['Movies', ['TV Series', 'BreakingBad.mp4', 'TheBigBangTheory.avi'], '1.avi', '22', '001.mp4']], 'tmp.txt', 'page.html'], '22'))
print(file_finderr(['home', ['Documents', ['FPRO', 'lists.txt', 'recursion.pdf', 'functions'], ['Python', 'hello_world.py', 'readme.md']], ['Downloads', ['Movies', ['TV Series', 'BreakingBad.mp4', 'TheBigBangTheory.avi'], '1.avi', '22', '001.mp4']], 'tmp.txt', 'page.html'], 'tuples.py'))
print(file_finderr(['home', ['Documents', ['FPRO', 'lists.txt', 'recursion.pdf', 'functions'], ['Python', 'hello_world.py', 'readme.md']], ['Downloads', ['Movies', ['TV Series', 'BreakingBad.mp4', 'TheBigBangTheory.avi'], '1.avi', '22', '001.mp4']], 'tmp.txt', 'page.html'], 'recursion.pdf'))
print(file_finderr(['user', ['Torrents', ['Movies', 'incredibles.mp4', 'mile22.mp4'], ['Books', 'how-to-think-like-a-computer-scientist.pdf']], ['Trabalhos', ['FPRO', 'RE09.py', 'RE10.py'], ['Alga', 'ex1.docx', 'ex2.docx']], 'a.out'], 'mile22.mp4'))
print(file_finderr(['user', ['Torrents', ['Movies', 'incredibles.mp4', 'mile22.mp4'], ['Books', 'how-to-think-like-a-computer-scientist.pdf']], ['Trabalhos', ['FPRO', 'RE09.py', 'RE10.py'], ['Alga', 'ex1.docx', 'ex2.docx']], 'a.out'], 'RE10.py'))


def file_finder(dirs, file_name):
    for i, v in enumerate(dirs[1:]):
        if v == file_name and i != (len(dirs) - 1) and type(dirs[i + 1]) != list:
            return dirs[0] + "/" + v
        elif type(v) == list:
            for ind, x in enumerate(v[1:]):
                if type(x) == str:
                    if x == file_name and ind != 0:
                        return dirs[0] + "/" + v + "/" + x
                elif type(x) == list:
                    b = file_finder(x, file_name)
                    if type(b) == str and file_name in b:
                        return dirs[0] + "/" + v[0] + "/" + b


print(file_finder(['home', ['Documents', ['FPRO', 'lists.txt', 'recursion.pdf', 'functions'], ['Python', 'hello_world.py', 'readme.md']], ['Downloads', ['Movies', ['TV Series', 'BreakingBad.mp4', 'TheBigBangTheory.avi'], '1.avi', '22', '001.mp4']], 'tmp.txt', 'page.html'], 'Documents'))
print(file_finder(['home', ['Documents', ['FPRO', 'lists.txt', 'recursion.pdf', 'functions'], ['Python', 'hello_world.py', 'readme.md']], ['Downloads', ['Movies', ['TV Series', 'BreakingBad.mp4', 'TheBigBangTheory.avi'], '1.avi', '22', '001.mp4']], 'tmp.txt', 'page.html'], 'page.html'))
print(file_finder(['home', ['Documents', ['FPRO', 'lists.txt', 'recursion.pdf', 'functions'], ['Python', 'hello_world.py', 'readme.md']], ['Downloads', ['Movies', ['TV Series', 'BreakingBad.mp4', 'TheBigBangTheory.avi'], '1.avi', '22', '001.mp4']], 'tmp.txt', 'page.html'], 'hello_world.py'))
print(file_finder(['home', ['Documents', ['FPRO', 'lists.txt', 'recursion.pdf', 'functions'], ['Python', 'hello_world.py', 'readme.md']], ['Downloads', ['Movies', ['TV Series', 'BreakingBad.mp4', 'TheBigBangTheory.avi'], '1.avi', '22', '001.mp4']], 'tmp.txt', 'page.html'], '22'))
print(file_finder(['home', ['Documents', ['FPRO', 'lists.txt', 'recursion.pdf', 'functions'], ['Python', 'hello_world.py', 'readme.md']], ['Downloads', ['Movies', ['TV Series', 'BreakingBad.mp4', 'TheBigBangTheory.avi'], '1.avi', '22', '001.mp4']], 'tmp.txt', 'page.html'], 'tuples.py'))
print(file_finder(['home', ['Documents', ['FPRO', 'lists.txt', 'recursion.pdf', 'functions'], ['Python', 'hello_world.py', 'readme.md']], ['Downloads', ['Movies', ['TV Series', 'BreakingBad.mp4', 'TheBigBangTheory.avi'], '1.avi', '22', '001.mp4']], 'tmp.txt', 'page.html'], 'recursion.pdf'))
print(file_finder(['user', ['Torrents', ['Movies', 'incredibles.mp4', 'mile22.mp4'], ['Books', 'how-to-think-like-a-computer-scientist.pdf']], ['Trabalhos', ['FPRO', 'RE09.py', 'RE10.py'], ['Alga', 'ex1.docx', 'ex2.docx']], 'a.out'], 'mile22.mp4'))
print(file_finder(['user', ['Torrents', ['Movies', 'incredibles.mp4', 'mile22.mp4'], ['Books', 'how-to-think-like-a-computer-scientist.pdf']], ['Trabalhos', ['FPRO', 'RE09.py', 'RE10.py'], ['Alga', 'ex1.docx', 'ex2.docx']], 'a.out'], 'RE10.py'))

