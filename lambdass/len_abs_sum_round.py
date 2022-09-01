"""
Len, Abs, Sum, Round

len() -> Retorna o tamanho (número de itens) de um iterável

abs() -> Retorna o valor absoluto de um número inteiro ou real. O valor real do número sem o sinal

sum() -> recebe um iterável e retorna a soma dos elementos incluindo o valor inicial
valor inicial default é 0

round() -> Retorna o npumero arredondado com 'n' após a casa decimal
se não for informado ele retorna o inteiro mais próximo do número
"""

# Exemplos len

print(len([1, 2, 3, 4, 5]))

print(len((1, 2, 3, 4, 5)))

print(len({1, 2, 3, 4, 5}))

print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))

print(len(range(0, 10)))

print(len('Andre Silveira'))

# Quando utilizamos o len() o python está fazendo o seguinte
# chamado de Dunder len
print('Andre Silveira'.__len__())


# Exemplos abs

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

# Exemplos sum

print(sum([1, 2, 3, 4, 5]))

# Mudando o default de 0 para 5 o resultado vai de 15 para 20
print(sum([1, 2, 3, 4, 5], 5))

print(sum((3.14, 234.2, 12.2)))
print(sum({1, 2, 3, 4, 5}))
print(sum({'a':1, 'b':2, 'c':3, 'd':4, 'e':5}.values()))

# Exemplos round()

print(round(50.6))
print(round(96.7))
print(round(105.2))
print(round(440.8))
print(round(225.3))
print(round(1.23123895815, 2)) # Duas casas decimais

