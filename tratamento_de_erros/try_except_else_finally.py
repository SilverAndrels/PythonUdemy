"""
try / except / else / finally

TODA entrada de dados deve ser tratada


# Exemplo utilizando else -> só executa se o erro não acontecer. 

try:
    num = int(input('Informe um número: '))
except ValueError as err:
    print('O valor precisar ser um número inteiro!')
else:
    print(f'Você digitou o número: {num}')

# Finally
O finally é sempre executado independente se houver erro ou não
geralmente utilizado para fechar ou desalocar recursos.
"""

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Um dos valores está incorreto'
    except ZeroDivisionError:
        return 'Não é possível fazer divisões por 0(zero)'

num1 = input('Digite o primeiro valor: ')
num2 = input('Digite o segundo valor: ')

print(dividir(num1, num2))

