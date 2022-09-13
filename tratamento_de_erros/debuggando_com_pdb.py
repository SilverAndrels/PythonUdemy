"""
Debuggando com PDB
PDB -> Python Debugger


comandos basicos PDB
l -> listar onde estamos no código
n -> próxima linha
p -> imprime variável
c -> continua a execução, finaliza o debugging


import pdb

nome = 'André'
sobrenome = 'Silveira'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Python'
final = nome_completo + ' faz o curso de ' + curso
print(final)

* A partir do python 3.7 não é necessário importar o pdb
basta usar o breakpoint()
"""

nome = 'André'
sobrenome = 'Silveira'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Python'
final = nome_completo + ' faz o curso de ' + curso
print(final)
