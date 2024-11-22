'''SubFile which acts as a module for application'''

from random import randint

def main(*a):
    '''Function counts all words with lating chars in them and returns their number'''
    cyrillic_to_latin = {
    'А': 'A', 'В': 'B', 'Е': 'E', 'К': 'K', 'М': 'M', 'Н': 'H', 'О': 'O', 'Р': 'P', 'С': 'C', 'Т': 'T', 'У': 'Y', 'Х': 'X',
    'а': 'a', 'е': 'e', 'о': 'o', 'р': 'p', 'с': 'c', 'у': 'y', 'х': 'x'
    }
    result = []
    word = True
    x = list(map(lambda x: x, a))
    for i in x:
        lis = []
        xy = 0
        for k in i:
            if word is True:
                if k in cyrillic_to_latin.values():
                    word = False
                    xy += 1
                    if len(lis) == 0:
                        lis.append(i)
                    if len(lis) == 1:
                        lis.append(xy)
                    if len(lis) == 2:
                        lis[1] = xy

            else:
                if k in cyrillic_to_latin.values():
#                    print(k)
                    xy += 1
                    lis[1] = xy
                if k == ' ':
                    word = True
        if len(lis) != 0:
            result.append(lis)

    print(result)
    string = ''
    for i in result:
        for k in i:
            string = string + str(k) + '\t'
        string = string + '\n'
    return string
