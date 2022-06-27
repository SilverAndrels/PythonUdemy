list1 = [1, 2, 3, 4, 5, 6, 7, 87, 102, 22, 3231, 24, 3341]
list2 = ['A', 'N', 'D', 'R', 'E', ' ', 'S', 'I', 'L', 'V', 'E', 'I', 'R', 'A']
list3 = []
list4 = list(range(11))
list5 = list('Andre Silveira')


# Achar um valor na lista
number = 55
if number in list4:
    print(f'Find the number {number}')
else:
    print(f"Don't find the number {number}")

# Ordenando uma lista
list1.sort()
print(list1)

# Quantas vezes um valor aparece na lista
print(list1.count(1))
print(list5.count('e'))

# Adicionar elementos na lista
# append adiciona um elemento por vez
print(list1)
list1.append(55)
print(list1)

# extend adiciona um elemento por vez, se usando assim com append é adicionado a lista como sublista
list1.extend([1, 2, 3])
print(list1)

# Inserir um novo elemento na lista passando o indice sem substituir o valor que esta no indice
list1.insert(2, 'Alguma coisa aqui')
print(list1)

# Juntar duas listas
# list6 = list1 + list2 criando uma lista e juntando 1 e 2 print(list6)
list1.extend(list2)  # Juntando a lista 1 com a 2
print(list1)

# Imprimir a lista invertida
list1.reverse()
print(list1)
# Outro jeito
print(list1[::-1])

# Copiando uma lista
list6 = list2.copy()
print(list6)

# Saber tamanho da lista
print(len(list2))

# Remover o ultimo elemento da lista
print(list5)
list5.pop()
print(list5)

# Remover elemento pelo índice
list5.pop(2)
print(list5)

# Remover todos os elementos da lista
print(list5)
list5.clear()
print(list5)

# Repetir elementos de uma lista
listcopy = list5 * 2
print(listcopy)

# Converter String para lista é utilizado o espaço da string para separar
name = 'Silver Andrels'
namelist = name.split()
print(namelist)
# Especificando oque vai ser usado para separar
name = 'Silver,Andrels'
namelist = name.split(',')
print(namelist)

# Converter uma lista em uma String
list6 = ['Silver', 'Andrels']
print(list6)
convertion = ' '.join(list6)
print(convertion)
# Coloca o '%' no lugar dos espaços
convertion = '%'.join(list6)
print(convertion)

# Iterando sobre as listas
sum = 0
for element in list1:
    print(element)
    sum += element
print(sum)
# Exemplo 2
package = []
product = ''

while product != 'exit':
    print("Insert a new product or 'exit' to exit: ")
    product = input().lower()
    if product != 'exit':
        package.append(product)

for product in package:
    print(f"The products are {product}")

# Utilizando variáveis em listas
numbers = [1, 2, 3, 4, 5]

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numbers = [num1, num2, num3, num4, num5]

# Acesso aos elementos de forma indexada
colors = ['Green', 'Yellow', 'Blue', 'White']
print(colors[0])
print(colors[1])
print(colors[2])
print(colors[3])
# Acesso aos elementos de forma idexada inversa
# Para entender melhor a forma inversa, pense em uma roda onde todos os elementos estão 'ligados'
print(colors[-1])
print(colors[-2])
print(colors[-3])
print(colors[-4])

# Gerar índice em um for
for i, color, in enumerate(colors):
    print(i, color)

# Outros métodos úteis

# Encontrar o índice de um elemento na lista
numbers = [5, 6, 2, 3, 1, 10, 22, 22]

# Em qual índice está o número 22
# Se há mais de um igual, retorna o índice do primeiro encontrado
print(numbers.index(22))

# Fazer busca dentro de um range 'dizendo' com o segundo valor, por qual índice começar
print(numbers.index(2, 1))  # Buscando a partir do índice 1
# Fazendo uma busca dentro de um range 'dizendo' inicio/fim
print(numbers.index(6, 0, 3))  # Busca o 6 entre o índice 0 e 3

# Slice de lista com o parâmetro 'inicio'
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[1:])  # Inicia no índice 1 e vai pegando todos os outros elementos
# Slice de lista com o parâmetro 'fim'
print(list[:2])  # Inicia em 0 e vai até o índice 2 -1
print(list[1:3])  # Inicia em 1 e vai até o índice 3 -1
# Slice de lista com o parâmetro 'passo'
print(list[1::2])  # Inicia em 1 e vai até o fim de 2 em 2
print(list[::-1])  # Inicia em 0 e iverte a lista voltando de -1 em -1

# Soma, Valor Máximo, Valor Mínimo, Tamanho
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(list))
print(max(list))
print(min(list))
print(len(list))

# Transformar lista em tupla
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list)
print(type(list))

tupla = tuple(list)
print(tupla)
print(type(tupla))

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 - Deep Copy
# Copy não interfere na lista criada quando usado o append, apenas na nova que é uma copia, chamado de Deep Copy
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list)

new = list.copy()
print(new)

new.append(4)
print(list)
print(new)

# Forma 2 - Shallow Copy
# Ambas as lista acabam sendo modificadas quando usado o append neste caso
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list)

new = list

print(new)

new.append(4)
print(list)
print(new)
