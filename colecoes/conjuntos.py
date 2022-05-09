'''
Conjuntos

Em python conjuntos são chamados de sets

- Sets não possuem valores duplicados
- Sets não possuem valores ordenados
- Elementos não são acessados via índice ou seja, conjuntos não são indexados
'''
# Definindo um conjunto

# Forma 1

s = set({1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10}) # Há valores repetidos

print(s)
print(type(s))
# O conjunto ignora o valor repetido e não da erro

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10}
print(s)
print(type(s))

# Verificar se determinado elemento está contido no conjunto
if 3 in s:
    print('I find the 3')
else:
    print("I don't the 3")

# Usos interessantes com sets

citys = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
print(citys)
print(len(citys))

# Precisamos saber quantas cidades diferentes há
print(len(set(citys)))

# Adicionando elementos em um conjunto
s = {1, 2, 3}
s.add(5)
print(s)

# Remover elementos de um conjunto
s = {1, 2, 3}
print(s)

# Forma 1
s.remove(3) # 3 é o valor, não o indice, conjuntos não são indexados
print(s)

# Forma 2
s.discard(2) # se o valor não for encontrada, ele simplesmente ignora, sem erros
print(s)

s = {1, 2, 3}

# Copiando um conjunto para outro

# Forma 1 - Deep copy
new = s.copy()
print(new)

new.add(4)
print(new)
print(s)

# Forma 2 - Shallow copy

new = s
new.add(4)

print(new)
print(s)

# Remover todos os itens de um conjunto
s.clear()
print(s)

# Métodos matemáticos dos conjuntos

python_students = {'Marcos', 'Patrícia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
java_students = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patrícia'}

# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando union (Recomendada)
students = python_students.union(java_students)
print(students)

# Forma 2 - Utilizando o caractere pipe |
students2 = python_students | java_students
print(students2)

# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Utilizando intersection

both = python_students.intersection(java_students)
print(both)

# Forma 2 - Utilizando o &
both2 = python_students & java_students
print(both2)

# Gerar um conjunto de estudantes de um curso que não está no outro

only_python = python_students.difference(java_students)
print(only_python)

only_java = java_students.difference(python_students)
print(only_java)
