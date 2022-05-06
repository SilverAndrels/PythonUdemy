'''
Mapas -> Conhecidos em python como dicionários
Dicionários em python são representados por {}
'''
values = {'jan': 120, 'fev': 150, 'mar': 450}
# Iterar sobre dicionários

# Mostra as chaves
for key in values:
    print(key)

# Mostra os valores
for key in values:
    print(values[key])

# Mostra chave/valor
for key in values:
    print(f'{key} : {values[key]}')

print(values.keys())

# Recomendado
for key in values.keys():
    print(values[key])

# Acessando os valores

print(values.values())

for x in values.values():
    print(x)

