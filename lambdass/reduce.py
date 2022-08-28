"""
Reduce

Do python3+ a função reduce() não é mais uma função built-in.
Tem que ser importada a partir do módulo 'functools'

reduce() funciona da seguinte forma:
Passo 1: r1 = f(a1,a2) # Aplica a função nos dois primeiros elementos da coleçaõ e guarda o resultado
Passo 2: r2 = f(r1,a3) # Aplica a função passando o resultado do passo 1 + o terceiro elemento e guarda o resultado
repetindo isso até o fim
"""
# Usando reduce() para multiplicar todos os números de uma lista

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar o reduce() precisamos de uma função que receba dois parâmetros

multi = lambda x, y: x * y
res = reduce(multi, dados)
print(res)

