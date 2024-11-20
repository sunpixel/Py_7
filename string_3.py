'''SubFile which acts as a module for application'''

from random import randint

def count(a):
    '''Thsi function take a string and counts the number of vowels in it'''
    x = randint(0, len(a) - 1)
    k = 0
    sub = a[x]  # Random character
    for i in a:
        if i == sub:
            k += 1
    print(f'Character: "{sub}", Count: {k}')
