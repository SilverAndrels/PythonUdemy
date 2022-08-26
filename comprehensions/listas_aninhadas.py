"""
Listas aninhadas == matrizes de outras linguagens
"""
# Exemplos

lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Como se fosse uma matriz 3 x 3

# Acessando os dados

print(lista[0][1]) # Acessando o número 2
print(lista[2][1]) # Acessando o número 8, pode ser usado tbm lista[2][-2]

# Iterando com loops em uma lista aninhada
for l in lista:
    for num in l:
        print(num)

# List Comprehension
[[print(valor) for valor in l] for l in lista]

# Outros exemplos

# Gerando um tabuleiro/matriz 3 x 3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais
print([['*' for i in range(1, 4)] for j in range(1, 4)])
