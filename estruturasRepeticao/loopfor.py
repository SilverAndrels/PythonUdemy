nome = 'André Silveira'
lista = [1, 2, 3, 4, 5]
numeros = range(1, 10) #precisa transformar em lista

#Exemplo 1 iterando String
for letra in nome:
    print(letra)
    
#Exemplo 2 iterando lista
for numero in lista:
    print(numero)
    
#Exemplo 3 iterando range
for numero in range(1, 10):
    print(numero)
    
for _, valor in enumerate(nome): #o _ é utilizado quando não preciso do resultado da "variavel..."
    print(valor)
    


quantity = int(input ("How many times the loop has to run ??"))
sum = 0

for n in range(1, quantity +1):
    number = int(input(f"Insert the {n}/{quantity} value: "))
    sum += number
print(f"The sum is {sum}") #para não pular linha usar ,end='' no print

#printando emojis
for _ in range(3):
    for num in range (1, 11):
        print('\U0001F60D' * num)
        