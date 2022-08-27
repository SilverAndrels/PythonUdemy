"""
Map

Com Map, fazemos mapeamento de valores para função
"""
from math import pi

def area(r):
    # Calcula a área de um círculo com raio 'r'
    return pi * (r ** 2)

print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma Comum
areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# Utilizando Map
# Map é uma função que recebe dois parâmetros:
# O primeiro é uma função e o segundo é um iterável
# Retorna um Map Object
areas = map(area, raios)
print(list(areas))

# Map Com Lambda
print(list (map(lambda r: pi * (r ** 2), raios)))

# Outro exemplo

# Graus em C e converte para F
cidades = [('São Paulo', 30), ('Berlim', 24), ('Kiev', 5), ('Curitiba', 10)]

c_para_f = lambda c: (c[0], round((9/5) * c[1] + 32))

print(list(map(c_para_f, cidades)))
