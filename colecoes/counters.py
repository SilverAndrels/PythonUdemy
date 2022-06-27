'''
Módulo Collections - Counter (Contador)

Collections -> High performance Container Datatypes

Counter -> recebe um iteravel como parametro e cria um objeto tipo collections counter
'''
# Utilizando o counter

from collections import Counter as c

# Exemplo 1

list = [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1, 1, 4, 4, 4, 4, 5, 5, 5, 10, 22, 55]

res = c(list)
print(type(res))
print(res)

# Exemplo 2
print(c('André Silveira'))

# Utilizando o counter

from collections import Counter as c

# Exemplo 3

text = """Leslie Hubert "Les" Holden foi um aviador e ás da aviação australiano durante a 
Primeira Guerra Mundial e, mais tarde, um aviador comercial. Natural da Austrália Meridional,
ele juntou-se à Cavalaria Leve Australiana em Maio de 1915, servindo no Egipto e em França.
Em Dezembro de 1916 Les Holden voluntariou-se para o Australian Flying Corps e qualificou-se 
como piloto."""

words = text.split()

res = c(words)
print(res)
# Encontrando as 5 palavras com maior ocorrencia no texto
print(res.most_common(5))
