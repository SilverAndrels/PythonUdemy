"""
**kwargs

Podería ser: **qualquernome

por convenção é chamado de: **kwargs

diferente do *args o **kwargs exige que seja utilizado parâmetros nomeados
e transforma esses parâmetros extras em dicionário.
"""
# Exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita do(a) {pessoa.title()} é {cor}')
        
cores_favoritas(andré='Preto')

# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome':'André', 'sobrenome':'Silveira'}
print(mostra_nomes(**nomes))
