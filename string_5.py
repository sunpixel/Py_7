'''SubFile which acts as a module for application'''

from random import randint

def main(*a):
    '''Function counts all words with lating chars in them and returns their number'''
    cyrillic_to_latin = {
    'А': 'A', 'В': 'B', 'Е': 'E', 'К': 'K', 'М': 'M', 'Н': 'H', 'О': 'O', 'Р': 'P', 'С': 'C', 'Т': 'T', 'У': 'Y', 'Х': 'X',
    'а': 'a', 'е': 'e', 'о': 'o', 'р': 'p', 'с': 'c', 'у': 'y', 'х': 'x'
    }
    count = 0
    acount = 0
    word = True
    x = list(map(lambda x: x, a))
    for i in x:
        for k in i:
            if word == True:
                if k in cyrillic_to_latin.values():
#                    print(k)
                    count += 1
                    acount += 1
                    word = False
            else:
                if k in cyrillic_to_latin.values():
#                    print(k)
                    acount += 1
                if k == ' ':
                    word = True
    return f'Total number of words conatining non cyrilic symbols is: {count}. Total number of cyrilic symbols is: {acount}'