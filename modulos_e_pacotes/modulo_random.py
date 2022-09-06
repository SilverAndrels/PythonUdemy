"""
Módulo random e oque são módulos

módulos em Python são nada mais que arquivos Python

"""
# Para utilizar apenas a função random():
from random import random

# random() gera um número entre 0 e 1.
print(random())


from random import random

for x in range(20):
    print(random())


# uniform() -> Gera um número entre os valores estabelecidos

from random import uniform

for y in range(10):
    print(uniform(1, 9)) # 9 não será incluído


# randint() - Gera um número inteiro entre os valores estabelecidos
from random import randint

for h in range(6):
    print(randint(1, 61), end=', ')


# choice() -> Mostra um valor aleatório entre um iterável
from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))


# shuffle() -> tem a função de embaralhar dados
from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

shuffle(cartas)
print(cartas)

