'''SubFile which acts as a module for application'''

from random import randint

def main(a, b, c):
    '''This function takes 3 arguments and returns a string'''
    x = [a, b, c]
    ret = [None, None, None]
    for i in x:
        if ret[0] is None and isinstance(i, str):
            try:
                float(i)
            except ValueError:
                ret[0] = i  # String value

        elif ret[1] is None and isinstance(i, (int, float)):
            ret[1] = i

        elif ret[2] is None:
            sqr = lambda x: x * x
            mult = lambda x: (x + ' ') * randint(1, 3)
            try:
                y = float(i)
                ret[2] = sqr(y)
            except ValueError:
                ret[2] = mult(i)
    return ret
