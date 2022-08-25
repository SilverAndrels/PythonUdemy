"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer, vc poderá chamar ele de qualquer coisa
desde que comece com *

Exemplo:
*xis

mas a convenção é utilizar o nome *args

O parâmetro *args utilizado em uma função coloca os valores extra informados
como entrada em uma tupla
"""
# Exemplo sem *args:

def soma_todos_os_numeros(num1, num2, num3):
    return num1 + num2 + num3

print(soma_todos_os_numeros(1, 2, 3))

def soma_todos_os_numeros(*args):
    '''
    versão 1:
    total = 0
    for num in args:
        total += num
    return total
    '''
    # já que é uma tupla:
    return sum(args)

print(soma_todos_os_numeros())
print(soma_todos_os_numeros(1, 2))
print(soma_todos_os_numeros(2, 3, 4, 5, 6))

def soma_todos_os_numeros(*args):
    return sum(args)

numeros = [1, 2, 3, 4, 5, 6, 7]

# Desempacotador para funcionar a lista números com o retorno tupla do args
print(soma_todos_os_numeros(*numeros))
'''
OBS: O asterisco  serve para 'informar' ao python que estamos
passando como argumento uma coleção de dados.
desta forma ele saberá que precisa desempacotar estes dados antes de usar
'''
