"""
Reversed

Não confundir com reverse(), esta só funciona com as listas

A função reversed() funciona com qualquer iterável

Sua função é inverter o iterável

A função reversed() retorna um iterável chamado list reverse iterator
"""

# Exemplos

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

# Podemos converter o elemento retornado para uma Lista, Tupla, Conjunto(set)

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# Conjunto, não é definido a ordem dos elementos
# Conjunto(set)
print(set(reversed(lista)))

# Podemos iterar sobre o reversed()
for letra in reversed('Andre Silveira'):
    print(letra, end='') # ende='' para vir tudo na mesma linha

print('\n')

# Fazendo o mesmo resultado sem o for
print(''.join(list(reversed('Andre Silveira')))) # ''.join() para transformar a lista em string

# Fazendo de forma mais fácil com slice de strings
print('\n'+'Andre Silveira'[::-1])

# Utilizando o reversed() para fazer um loop ao contrário
for n in reversed(range(0, 10)):
    print(n, end='')

print('\n')

# Fazendo o loop ao contrário usando apenas o range()
for n in range(9, -1, -1):
    print(n, end='')

