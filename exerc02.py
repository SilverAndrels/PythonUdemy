'''
Programa que pede um número ao usuário e se positivo,
calcula a raiz, se negativo printa que é inválido
'''
#importando math para usar sqrt para fazer cálculo da raiz
import math
#pedindo um número ao usuário
num = float(input("Digite o número: "))
#lógica
if num > 0:
    raiz = math.sqrt(num)
    print(raiz)
else:
    print("O número digitado é inválido")
