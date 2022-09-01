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
print(list(zip1))

