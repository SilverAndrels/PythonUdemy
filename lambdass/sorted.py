"""
Sorted

Não confundir com a função sort() -> esse só funciona em listas

Podemos utilizar o sorted() com qualquer iterável
Como o nome já diz, sorted() é usado para ordenar
O sorted() sempre rertorna uma lista

# Exemplo
numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros)) # Do menor para o maior

# Adicionando parâmetros ao sorted()
numeros = [6, 1, 8, 2]

print(sorted(numeros, reverse=True)) # Ordena os números do maior para o menor


# Utilizando sorted() em coisas mais complexas

usuarios = [{"username":"Carlos", "tweets":["eu amo café", "eu amo me exercitar"]},
            {"username":"Adevilson", "tweets":["comprei um fusca", "eu não gosto do calor"]},
            {"username":"Lilith", "tweets":["tbm gosto de java", "python é muito bom",
                                            "Gosto do Batman"]},
            {"username":"Lucifer", "tweets":[]}
]

# Para ordenar e imprimir com sorted() e dictionary

# Ordena os usuários pelo nome me ordem alfabética
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Ordenando pelo número de tweets -> maior pro menor -> para fazer o contrário reverse=True
print('\n', sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))


"""

# Último exemplo

musicas = [
    {"titulo": "Thunderstruck", "tocada": 312},
    {"titulo": "You should see me in a crown", "tocada": 250},
    {"titulo": "Envolver", "tocada": 30000},
    {"titulo": "Dinero", "tocada": 20},
    {"titulo": "New rules", "tocada": 1000},
    {"titulo": "Fancy", "tocada": 320},
    {"titulo": "Peaches", "tocada": 2500},
    {"titulo": "Hot N Cold", "tocada": 120},
    {"titulo": "Black Magic", "tocada": 450},
]

# Ordenando da música menos tocada para a mais
print(sorted(musicas, key=lambda musica: musica["tocada"]))

# Ordenando da música mais tocada para a menos
print('\n', sorted(musicas, key=lambda musica: musica["tocada"], reverse=True))

