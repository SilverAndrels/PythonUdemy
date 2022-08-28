"""
Set Comprehension

diferença de lista para um set VISUALMENTE é o {}
"""
lista = [1, 2, 4]
set = {1, 2, 4}

# Exemplo

# numeros = {x ** 2 for x in range(10)} não é necessário armazenar em uma variável
print({x ** 2 for x in range(10)})
