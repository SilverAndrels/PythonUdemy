"""
Filter

Filter serve para filtrar dados de uma determinada coleção.

# Biblíoteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de um sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Utilizando mean() para calcular a média
media = statistics.mean(dados)

print(media)
# OBS: Assim como a função map() a filter() tbm recebe dois parâmetros
# uma função e um iterável

res = filter(lambda x: x > media, dados)
print(list(res))

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
# Melhor forma de fazer
res = filter(None, paises)

# Forma 'piorada'
# res = filter(lambda pais: len(pais) > 0, paises)

# Outra forma, com lambda
# res = filter(lambda pais: pais != '', paises)

print(list(res))
"""
