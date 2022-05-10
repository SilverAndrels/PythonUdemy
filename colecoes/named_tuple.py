'''
Módulo Collections - Named Tuple

# Recapitulando tupla
values = (1, 2, 3)

print(values[1])

Named Tuple -> são tuplas diferentes onde especificamos nome e paramêtros
'''
from collections import namedtuple as nt

# Forma 1 - Declaração Named Tuple

dog = nt('dog', 'age name breed')

# Forma 2 - Declaração Named Tuple

dog = nt('dog', 'age, name, breed')

# Forma 3 - Declaração Named Tuple

dog = nt('dog', ['age', 'name', 'breed'])

# Usando

charles = dog(age=2, name='charles', breed='Husky')
print(charles)

# Acessando os dados
# Forma 1

print(charles[0]) # idade
print(charles[1]) # nome
print(charles[2]) # raça

# Forma 2

print(charles.age)
print(charles.name)
print(charles.breed)
