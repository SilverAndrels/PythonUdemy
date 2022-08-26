"""
Dictionary Comprehension

Sintaxe
{chave:valor for valor in i}
"""
# Exemplos

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

nums = (1, 2, 3, 4, 5, 6, 100)

quadrados = {valor: valor ** 2 for valor in nums}
print(quadrados)

chaves = 'abcdef'
valores = [1, 2, 3, 4, 5, 6]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 21]

res = {num: ('par' if not num % 2 else 'impar') for num in numeros}
print(res)
