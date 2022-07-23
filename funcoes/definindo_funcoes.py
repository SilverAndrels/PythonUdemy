'''

Definindo Funções

- Funções são pequenas partes de código que realizam tarefas específicas;
- Pode ou não receber entrada de dados e retornar uma saída de dados;

Funções  já utilizadas;
- print()
- len()
- min()
- max()
- count()
etc...
'''
# Exemplo utilizando funções

colors = ['green', 'yellow', 'blue', 'white']

# Utilizando a função integrada (Built-in) do python

print(colors)

colors.append('cyan blue')
print(colors)

# Como definir funções
'''
Forma geral de definir uma função

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao
'''
# Utilizando funções

def say_hi():
    print('hi')
    
# Chamando a função
# Sem o parênteses a função não é executada!
say_hi()

