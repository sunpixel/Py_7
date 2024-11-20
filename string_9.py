'''SubFile conatining a module for application'''

from random import randint

def main(a):
    '''Mina function of a subfile'''
    print(reverse(a))
    print(find_char(a))
    print(format(a))

def reverse(a):
    '''Reverses a string'''
    return a[::-1]

def find_char(a):
    '''Finds a random char in a string'''
    x = randint(0, len(a) - 1)
    x = a[x]
    y = a.find(x)
    return f'Char "{x}" is found at index {y}'

def format(a):
    '''Formats a string'''
    a = a.strip()
    a = a.lower()
    a = a.replace(' ', '_')
    a = f'Formatted string: {a}'
    return a
