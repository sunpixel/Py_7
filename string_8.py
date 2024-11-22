'''SubFile conatining a module for application'''

def replace_char(a):
    '''replaces a certain char in a string'''
    char = ['.', '?', '!']
    x = 0
    string = ''
    a = list(a)
    while x < len(a) - 1:
        if a[x] in char and a[x+1] != a[x]:
            a[x] = '\n'
        string += a[x]
        x += 1
    string = string.replace('.', '')
    string = ' ' + string
    return string
