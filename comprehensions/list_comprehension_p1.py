"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados
processados a partir de outro iterável.

# Sintaxe:
[ x for x in i ]
"""
# Exemplos

numeros = [1, 2, 3, 4, 5]

res = [ num * 10 for num in numeros ]

print(res)

# - A primeira parte é: for num in numeros
# - A segunda parte é: num * 10


res = [num / 2 for num in numeros]
print(res)

def quadrado(valor):
    return valor ** 2

res = [quadrado(num) for num in numeros]
print(res)

# List Comprehension vs Loop

# Loop
numeros = [1, 2, 3, 4, 5, 7]

numeros_dobrados = []

for num in numeros:
    numeros_dobrados.append(num * 2)
    
print(numeros_dobrados)    

# List Comprehension
print([num * 2 for num in numeros])

# Outros exemplos

# 1
nome = 'André Silveira'
print([letra.upper() for letra in nome])

# 2
def maiuscula(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

amigos = ['carlos', 'eduardo', 'patrick']
print([maiuscula(amigo) for amigo in amigos])

# 3
print([num * 3 for num in range(1, 10)])

# 4
print([str(numero) for numero in [1, 2, 3, 4, 5]])
