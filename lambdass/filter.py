"""
Filter

Filter serve para filtrar dados de uma determinada coleção.
"""
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

# Diferença entre Map e Filter:
# map() -> uma função e um iterável e retorna um objeto mapeando a função
# para cada elemento do iterável

# filter() -> uma função e um iterável e retorna um objeto filtrando
# apenas os elementos de acordo com a função

# map() retorna outros valores
# filter() retorna True ou False

# Exemplo mais complexo

usuarios = [{"username":"carlos", "tweets":["eu amo café", "eu amo me exercitar"]},
            {"username":"adevilson", "tweets":["comprei um fusca", "eu não gosto do calor"]},
            {"username":"Lilith", "tweets":["tbm gosto de java", "python é muito bom"]},
            {"username":"Lucifer", "tweets":[]}
]

# Filtrar os usuários que estão inativos
# Forma 1
# inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))
# print(inativos)

# Forma 2
inativos = list(filter(lambda u: not u['tweets'], usuarios))
print(inativos)


# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria', 'Raimunda']

#retorna uma lista com o nome da instrutora se tiver menos de 5 letras
instrutora = list(map(lambda n: f'Sua instrutora é a: {n}', filter(lambda n: len(n) < 5, nomes))
print(instrutora)

