"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos
min() -> Retorna o menor valor em um iterável ou o menor de dois ou mais elementos

# Exemplos
# Pode ser qualquer iterável, tupla, lista, set...

"""

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))

tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla))

conjunto = {1, 8, 4, 99, 34, 129} # set
print(max(conjunto))

# Dicionáro sem o .values() retorna a chave primeiro, nesse caso 'f'
dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario))

# Dicionáro utilizando o .values() agora, retorna o valor 129
dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario.values()))

# Programa que recebe dois valores do usuário e mostra o maior

numero_1 = int(input('Digite o primeiro valor: '))
numero_2 =  int(input('Digite o segundo valor: '))

print(f'O maior valor é: {max(numero_1, numero_2)}')


# Exemplos min()
# Pode ser qualquer iterável, tupla, lista, set...

lista = [1, 8, 4, 99, 34, 129]
print(min(lista))

tupla = (1, 8, 4, 99, 34, 129)
print(min(tupla))

conjunto = {1, 8, 4, 99, 34, 129} # set
print(min(conjunto))

# Dicionáro sem o .values() retorna a chave primeiro, nesse caso 'a'
dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario))

# Dicionáro utilizando o .values() agora, retorna o valor 1
dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario.values()))

# Programa que recebe dois valores do usuário e mostra o menor

numero_1 = int(input('Digite o primeiro valor: '))
numero_2 =  int(input('Digite o segundo valor: '))

print(f'O menor valor é: {min(numero_1, numero_2)}')


# Outros exemplos
# Neste caso irá imprimir Tim e Arya pq ele está considerando a ordem alfabética
nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Olivander']

print(max(nomes)) # Tim
print(min(nomes)) # Arya

print(max(nomes, key=lambda nome: len(nome))) # Olivander
print(min(nomes, key=lambda nome: len(nome))) # Tim


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

# Retorna a música mais tocada
print(max(musicas, key=lambda musica: musica["tocada"]))

# Retorna a música menos tocada
print(min(musicas, key=lambda musica: musica["tocada"]))

# Para imprimir apenas os títulos das músicas mais e menos tocada
print(max(musicas, key=lambda musica: musica["tocada"])["titulo"])
print(min(musicas, key=lambda musica: musica["tocada"])["titulo"])

# Forma mais "convensional" sem max, min ou lambda

max = 0
for musica in musicas:
    if musica["tocada"] > max:
        max = musica["tocada"]

for musica in musicas:
    if musica["tocada"] == max:
        print(musica["titulo"])

min = 10000000
for musica in musicas:
    if musica["tocada"] < min:
        min = musica["tocada"]

for musica in musicas:
    if musica["tocada"] == min:
        print(musica["titulo"])


