'''SubFile conatining a module for application'''

def polindrom(a):
    '''Function checks if the string is a polindrom'''
    a = a.lower()
    a = a.replace(' ', '')
    if a == a[::-1]:
        return 'The string is a polindrom'
    else:
        return 'The string is not a polindrom'
