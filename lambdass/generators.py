"""
Generators

Tuple Comprehensions se chamam na vdd Generators
"""
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))


nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

# List Comprehensions
res = [nome[0] == 'C' for nome in nomes]
print(res)

# Generator - Consome menos recursos do que os 'Comprehensions'
res = (nome[0] == 'C' for nome in nomes)
print(type(res))

# Utilidade do getsizeof() -> Retorna a quantidade de bytes em memória do elemento passado
from sys import getsizeof

# Mostrando quantos bytes a string abaixo tem em memória
print(getsizeof('Andre Silveira'))

from sys import getsizeof

# Gerando uma lista de números usando List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dictionary Comprehension
dictionary_comp = getsizeof({x: x * 10 for x in range(1000)}

# Gerando uma lista de números com Generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastam em memória:')

