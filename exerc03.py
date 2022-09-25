''''
pede um número ao usuário e imprime a soma de cada caractere 251 (2 + 5 + 1) = 8
'''

soma = 0
# pedindo um número inteiro maior que zero ao usuário
num = input("Digite um número inteiro: ")
# lógica
if int(num) < 0:
    print("Número inválido!")
elif int(num) > 0:
    soma = (sum(int(num) for num in num))
    print(f"Soma do número digitado é: {soma}")
