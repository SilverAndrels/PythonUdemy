"""
r - abre para leitura (padrão)
w - abre para escrita e sobrescreve caso já exista
x - abre para escrita apenas se o arquivo não existir, gera FileExistsError
a - abre para escrita adiciona na ultima linha caso exista
"""

try:
    with open('abc.txt', 'x') as narquivo:
        narquivo.write('teste01')
except FileExistsError:
    print('O arquivo já existe !')

