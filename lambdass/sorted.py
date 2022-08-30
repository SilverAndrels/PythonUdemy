"""
Sorted

Não confundir com a função sort() -> esse só funciona em listas

Podemos utilizar o sorted() com qualquer iterável
Como o nome já diz, sorted() é usado para ordenar
O sorted() sempre rertorna uma lista

# Exemplo
numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros)) # Do menor para o maior

"""

# Adicionando parâmetros ao sorted()
numeros = [6, 1, 8, 2]

print(sorted(numeros, reverse=True)) # Ordena os números do maior para o menor

