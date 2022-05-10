'''
Módulo Collections - Deque

Podemos dizer que é uma lista de alta performance
'''
from collections import deque as d

deq = d('ndr')
print(deq)

# Adicionando elementos no deque

deq.append('é') # Adiciona no final
print(deq)

deq.appendleft('A') # Adiciona no começo
print(deq)

# Remover elementos

print(deq.pop()) # Remove e retorna o último elemento

print(deq)

print(deq.popleft()) # Remove e retorna o primeiro elemento

print(deq)
