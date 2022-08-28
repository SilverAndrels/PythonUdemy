"""
List Comprehension part 2

Nós podemos adicionar estruturas condicionais lógicas às nossas list comprehension
"""

# Exemplos

# 1
numeros = [2, 3, 5, 6, 7, 8, 10, 12]

pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]
print(f"Os pares são: {pares} e os ímpares: {impares}")

# Refatorado

# Qualquer número par % 2 é 0. O zero em python é False. if not False == True:
pares = [num for num in numeros if not num % 2]

# Qualquer número impar % 2 é 1. O 1 em python é True:
impares = [num for num in numeros if num % 2]

print(f"Os pares são: {pares} e os ímpares são: {impares}")

# 2
res = [num * 2 if num % 2 == 0 else num / 2 for num in numeros]
print(res)
