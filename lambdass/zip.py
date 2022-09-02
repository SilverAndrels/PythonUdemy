"""
Zip

zip() -> cria um iterável (Zip Object)
agrega um elemento de cada um dos iteráveis passados na entrada como pares.

[1, 4] [2, 5] [3, 6]
"""
# Exemplos zip()

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)

# Sempre podemos gerar uma lista, tupla, conjunto(set), dicionário
print(list(zip1))

lista3 = [7, 8, 9, 10, 11]

zip1 = zip(lista1, lista2, lista3)

# como a lista3 é maior que as outras os números sem correspondentes são 'ignorados'
# o zip() usa sempre o menor 'tamanho' entre os iteráveis, o 10 e 11 sempre vão ser 'ignorados'
# independente da ordem.
print(list(zip1))


# Podemos utilizar diferentes iteráveis com zip()

tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# Lista de tuplas

dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados)))


# Outro exemplo

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]

alunos = ['Marcia', 'Pedro', 'Carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

print(final)

# Utilizando o map()

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))

