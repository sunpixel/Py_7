'''SubFile conatining a module for application'''

from random import randint

def main(a, b):
    '''Prints a string from 2 arguments'''
    a = str(a)
    b = str(b)
    x = lambda x, y: (x + ' ' + y + '\n') * randint(1, 10)
    print(x(a, b))
