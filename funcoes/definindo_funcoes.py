'''
Definindo Funções

- Funções são pequenas partes de código que realizam tarefas específicas;
- Pode ou não receber entrada de dados e retornar uma saída de dados;

Funções  já utilizadas;
- print()
- len()
- min()
- max()
- count()
etc...
'''

# Exemplo utilizando funções

colors = ['green', 'yellow', 'blue', 'white']

# Utilizando a função integrada (Built-in) do python

print(colors)

colors.append('cyan blue')
print(colors)

# Como definir funções
'''
Forma geral de definir uma função

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao
'''
# Utilizando funções

def say_hi():
    print('hi')

# Chamando a função
# Sem o parênteses a função não é executada!
say_hi()

# Funções com retorno
# - O return finaliza a função, nada após ele é executado

def square_of_7():
    return 7 * 7

ret = square_of_7()

print(f'Return {ret}')
# ou
print(f'Return {square_of_7()}') # Melhor jeito

# Neste caso abaixo ele retorna o 4.

def new_function():
    var = True
    if var:
        return 4
    elif var is None:
        return 3.2
    return 'b'

print(new_function())


def other_function():
    return 2, 3, 4, 5

n1, n2, n3, n4 = other_function()

print(n1, n2, n3, n4)

# Função "joga moeda"

from random import random as r

def throw_coin():
    if r() > 0.5:
        return 'Cara'
    return 'Coroa'

print(throw_coin())
