'''
- Funções com parâmetro (de entrada)
- Funções que recebem dados para serem processados
'''

# Refatorando uma função

'''
def square_of_7():
    return 7 * 7

ret = square_of_7()

print(f'Return {ret}')
# ou
print(f'Return {square_of_7()}')

# melhor jeito abaixo

number = int(input('Insert the number: '))

def square(number):
    # return number * number
    return number ** 2

print(square(number))
'''

# Funções podem ter n parâmetros de entrada. Ou seja, podemos receber como entrada
# em uma função quantos parâmetros forem necessários. Eles são separados por vírgula.

# Exemplos

def sum(a, b):
    return a + b

def mult(num1, num2):
    return num1 * num2

def other(num1, b, msg):
    return (num1 + b) * msg

print(sum(2, 4))
print(mult(2, 10))
print(other(3, 2, 'salve\n'))
