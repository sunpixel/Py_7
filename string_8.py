'''SubFile conatining a module for application'''

def replace_char(a):
    '''replaces a certain char in a string'''
    char = ['.', '?', '!']
    for i in a:
        if i in char:
            a = a.replace(i, '\n')
    a = a.strip()
    a = ' ' + a
    return a