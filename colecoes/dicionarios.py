'''
Dicionários

Em python os dicionários são conhecidos como 'mapas'
Dicionários são coleções do tipo chave/valor
Dicionários são representados por {}
Tanto chave quanto valor podem ser de qualquer tipo
Não pode ter chaves repetidas
'''
# {'chave':'valor', 'chave':'valor'...}
# Forma 1 (mais comum - Recomendada)
countrys = {'br': 'Brazil',
            'usa': 'United States of America', 'pt': 'Portugal'}
print(countrys)
print(type(countrys))

# Forma 2 (menos comum)
countrys = dict(br='Brazil', usa='United States of America', pt='Portugal')
print(countrys)
print(type(countrys))

countrys = {'br': 'Brazil',
            'usa': 'United States of America', 'pt': 'Portugal'}
# Acessando elementos

# Forma 1 - Acessando via chave
print(countrys['br'])

# Forma 2 - Acessando via get - Recomendada
print(countrys.get('br'))

countrys = {'br': 'Brazil',
            'usa': 'United States of America', 'pt': 'Portugal'}
# Verificar se determinada chave se encontra no dicionário
print('br' in countrys)
print('ru' in countrys)
print('United States of America' in countrys)

if 'ru' in countrys:
    russia = countrys['ru']

# Adicionando elementos em um dicionário
values = {'jan': 120, 'fev': 150, 'mar': 450}
print(values)
print(type(values))

# Forma 1 - (mais comum)
values['abr'] = 220
print(values)

# Forma 2
new_data = {'mai': 500}
values.update(new_data)  # values.update({'mai':500})
print(values)

# Atualizando dados de um dicionário

# Forma 1
values['mai'] = 550
print(values)

# Forma 2
values.update({'mai': 600})
print(values)

# Remover dados de um dicionário
values = {'jan': 120, 'fev': 150, 'mar': 450}

# Forma 1 - (mais comum)
values.pop('jan')
print(values)

# Forma 2
del values['fev']
print(values)

# Métodos de dicionários
d = {'a': 1, 'b': 2, 'c': 3}
print(d)
# Limpar dicionário
d.clear()
print(d)

# Copiando um dicionário para outro
d = {'a': 1, 'b': 2, 'c': 3}

# Forma 1 - # Deep copy
new = d.copy()  # Deep copy
print(d)
print(new)

new['d'] = 4
print(d)
print(new)

# Forma 2 - # Shallow copy
d = {'a': 1, 'b': 2, 'c': 3}

new = d
print(new)

new['d'] = 4
print(d)
print(new)
