'''
Modulo Collections - Ordered dict
'''
# Dicionário normal não é garantida a ordem dos números
from collections import OrderedDict as od
dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for key, value in dictionary.items():
    print(f'key={key}: value={value}')


# Ordered dict garante a ordem de inserção dos elementos


dictionary = od({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for key, value in dictionary.items():
    print(f'key={key}: value={value}')
