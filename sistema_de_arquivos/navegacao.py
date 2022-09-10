"""
import os
A VERSÃO DO CURSO NÃO FUNCIONA ENTÃO FIZ ASSIM!
# getcwd() pega o diretório atual e retorna o path absoluto

print(os.getcwd())

# Para mudar de diretório

os.chdir('..')

print(os.getcwd())


"""
import os
path = ''
directory = 'teste'

path = os.path.join(os.getcwd(), directory)
print(os.getcwd())
os.mkdir(path)
#res = os.path.join(os.getcwd(), 'teste')

os.chdir(path)

print(os.getcwd())

