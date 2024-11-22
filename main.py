'''Main execuatble file of a program'''

# Importing modules

from random import randint
import string_1
import string_2
import string_3
import string_5
import string_6
import string_7
import string_8
import string_9

if __name__ == '__main__':
    print('=' * 40)
    print(string_1.main('Hello', 1, 'Sunshine'))
    print('=' * 40)
    string_2.main('Hello', 'Sunshine')
    print('=' * 40)
    string_3.count('Hello, Sunshine')
    print('=' * 40)
    fun = lambda x: x[1:randint(2, len(x) - 2)] # Number 4
    print(fun('Hello, Sunshine'))
    print('=' * 40)
    print(string_5.main('Hello, Sunshine', 'Привет, Солнце', 'Привет, Sunshine', 'Привет'))
    print('=' * 40)
    print(string_6.polindrom('level'))
    print(string_6.polindrom('elevator'))
    print('=' * 40)
    string_7.extra('   Hello,   a   Sunshine   ')
    print('=' * 40)
    print(string_8.replace_char('Hello, Sunshine... This ia a good day. Right?'))
    print('=' * 40)
    string_9.main('Hello, Sunshine')
    print(string_5.main('Hellо, friеnd', 'Hоw arе уu?' ))
