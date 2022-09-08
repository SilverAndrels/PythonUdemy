"""
seek() -> utilizada para movimentar o cursor pelo arquivo
"""
arquivo = open('txt.txt')
print(arquivo.read())

# move o cursor para o começo do arquivo.
arquivo.seek(0)

print(arquivo.read())

# readline() -> lê o arquivo linha a linha

a = arquivo.readline()
print(a)

# readlines()

linhas = arquivo.readlines()

print(len(linhas))


# Abrindo o arquivo
arquivo = open('txt.txt')

# Para fechar o arquivo
arquivo.close()

