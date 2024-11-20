'''SubFile conatining a module for application'''

def extra(a):
    '''function deletes extra spaces in a string'''
    print(f'Original string is: {a} and its lenght is {len(a)}')
    a = a.strip()   # deletes spaces at the beginning and at the end of a string
    a = a.split()   # splits the string
    a = ' '.join(a)
    print(f'Extra spaces are deleted: {a} and new lenght is {len(a)}')
