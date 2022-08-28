"""
Utilizando Lambdas (Expressões Lambdas, são funções sem nome ou seja, funções anônimas)

# Função 'normal' em python

def funcao(x):
    return 3 * x + 1

print(funcao(10))

# Expressão Lambda

lambda x: 3 * x + 1
"""
# Podemos ter expressões lambdas com múltiplas entradas ou nenhuma

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('andré', 'silveira'))

lambda_sem_entrada = lambda : 'Esta função lambda não tem parâmetro de entrada e retorna esta string'

lambda_uma_entrada = lambda x: x * 10 + 2

lambda_duas_entradas = lambda x, y: (x + y) * 100

print(lambda_sem_entrada())
print(lambda_uma_entrada(2))
print(lambda_duas_entradas(2, 3))

# Ordenando por sobrenome usando sort + lambda
autores = ['Galileu Galilei', 'Johannes Kepler', 'Isaac Newton', 'Nikola Tesla', 'Albert Einstein',
           'Michael Faraday', 'James Maxwell']

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)

# Função Quadrática

# Definindo a função

def gerador_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c

teste = gerador_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(gerador_funcao_quadratica(6, -4, 5)(-2)) # 2 é o valor de X para a lambda
