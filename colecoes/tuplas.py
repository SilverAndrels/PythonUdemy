'''
1 - Representadas por () parênteses
2 - tuplas são imutáveis, ou seja toda operação em uma tupla, cria uma nova
'''
# Cuidado 1: ambos abaixo são considerados tuplas
tuple1 = (1, 2, 3, 4, 5, 6)
print(tuple1)
print(type(tuple1))

tuple2 = 1, 2, 3, 4, 5, 6
print(tuple2)
print(type(tuple2))

# Cuidado 2: Tupla com 1 elemento
tuple3 = (4)  # É considerado como int, não como tupla
print(tuple3)
print(type(tuple3))

tuple4 = (4,)  # Já esse é considerado uma tupla de um elemento
print(tuple4)
print(type(tuple4))

tuple5 = 4,  # Também é uma tupla, o mais importante é a vírgula
print(tuple5)
print(type(tuple5))

# Gerando uma tupla dinamicamente com o range(inicio, fim, passo)
tuple1 = tuple(range(10, 50, 2))
print(tuple1)
print(type(tuple1))

# Desempacotamento de tupla
# Número de elementos e 'variáveis' tem que ser iguais
tuple1 = ('André', 'Silveira')
name, midle_name = tuple1
print(name)
print(midle_name)

# Como as tuplas são imutáveis, não há métodos para adição e remoção de elementos

# Soma, Valor Máximo, Valor Mínimo e tamanho
# Se os valores forem todos inteiros ou reais

tuple1 = (1, 2, 3, 4, 5, 6, 90)
print(sum(tuple1))
print(max(tuple1))
print(min(tuple1))
print(len(tuple1))

# Concatenação de tuplas
# Tuplas são imutáveis
tuple1 = 1, 2, 3, 4, 5
print(tuple1)

tuple2 = 6, 7, 8, 9, 10
print(tuple2)

print(tuple1 + tuple2)

print(tuple1)
print(tuple2)

tuple1 += tuple2  # Podemos sobrescrever seus valores
print(tuple1)

# Verificar se há determinado elemento na tupla
tuple1 = (1, 2, 3, 4)
print(2 in tuple1)

# Iterando sobre uma tupla
tuple1 = (1, 2, 3, 4)
for n in tuple1:
    print(n)

for i, valor in enumerate(tuple1):
    print(i, valor)

# Contando elementos dentro de uma tupla
tuple1 = ('a', 'b', 'c', 'd', 'a', 'b', 'c', 'w')
print(tuple1.count('a'))

# Dicas na utilização de tuplas
# Sempre que não precisarmos mudar os dados usamos tuplas
# Exemplo
months = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')
# O acesso aos itens de uma tupla são semelhantes ao de uma lista
print(months[5])

# Iterar com while
i = 0
while i < len(months):
    print(months[i])
    i += 1

# Verificar em qual índice está o elemento
print(months.index('August'))

months = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')
# Slicing
# tupla[inicio::fim::passo]
print(months[5:9])

# Por quê utilizar tuplas ?
# - Tuplas são mais rápidas que listas
# - Tuplas deixam seu código mais seguro, já que são imutáveis

# Copiando uma tupla para outra
tuple1 = (1, 2, 3)
print(tuple1)

new = tuple1
print(new)
