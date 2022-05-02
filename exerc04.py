''''
verifica um número inteiro e mostra se é divisivel por 3 ou por 5 mas nao
simultaneamente pelos dois
'''
num = 0
# pedindo um número inteiro para o usuário
num = int(input("Digite um número inteiro: "))
if num % 3 == 0:
    print(f"{num} é divisível por 3!")
else:
    print(f"{num} é divisível por 5!")
