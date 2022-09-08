"""
Bloco with

"""

# O 'contexto' é fechado após execução do whith
# então não é necessário fechar o arquivo


with open('txt.txt') as text:
    print(text.readlines())

