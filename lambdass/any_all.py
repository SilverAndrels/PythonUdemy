"""
Any e All

all() -> Retrona True, se todos os elementos dos iterável são verdadeiros ou se o iterável
está vazio
"""

# Exemplo all()

print(all([0, 1, 2, 3, 4, 5, 6])) # Como 0 é False o all() retorna False
print(all([1, 2, 3, 4, 5, 6])) # Como todos são True o all() retorna True
print(all([])) # Como a a lista está vazia o all() retorna True

nomes = ['Carlos', 'Camila', 'Célia', 'Cícero']

print(all([nome[0] == 'C' for nome in nomes])) # Como todos da lista começam com 'C' então True

#OBS: Um iterável vazio convertido em boolean é Flase, mas o all() entende como True

print(all(letra for letra in 'eio' if letra in 'aeiou')) # Vefirica se 'eio' está em 'aeiou'

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))


# any(): Retorna True se qualquer elemento do iterável for verdadeiro. se o iterável estiver vazio
# retorna False

print(any([0, 1, 2, 3, 4])) # O any() retorna True neste caso

