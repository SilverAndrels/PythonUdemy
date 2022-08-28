"""
Funções com parâmetro padrão (Default parameters)

Funções onde a passagem de parâmetro seja opcional;
Exemplo de função com parâmetro opcional
print('Abcd')
print()

Exemplo de função com parâmetro obrigátório
def quadrado(numero):
    return numero ** 2
    
print(quadrado(3))
print(quadrado()) # TypeError
"""
def exponencial(numero, potencia=2):
    return numero ** potencia

print(exponencial(2, 3))
print(exponencial(3))  # por padrão eleva ao quadrado
print(exponencial(3, 5))  # eleva á potência informada pelo usuário

# Outros exemplos

def soma(num1=0, num2=1):
    return num1 + num2

print(soma(2, 3))
print(soma(4))
print(soma())

def monstra_informacao(nome='Python', instrutor = False):
    if nome == 'Python' and instrutor:
        return 'Bem vindo!'
    elif nome == 'Python':
        return 'Pensei que era o Python'
    return f'Olá {nome}'

print(monstra_informacao())
print(monstra_informacao(instrutor=True))
print(monstra_informacao('André'))

def soma(a, b):
    return a + b

def mat(a, b, fun=soma):
    return fun(a, b)

def subtracao(a, b):
    return a - b

print(mat(2, 10))
print(mat(2, 10, subtracao))
