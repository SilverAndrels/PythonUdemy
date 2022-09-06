"""
O bloco try/except

Utilizamos este bloco para tratar erros.
previnindo que o programa pare de funcionar e o usuário
recebe mensagens de erro inesperadas.

# Forma geral mais simples:

try:
    //execução que pode gerar um problema.
except:
    //oque deve ser feito caso o problema ocorra.


# Tratando um erro genérico

try:
    geek()
except:
    print('Deu algum problema!!!')

# SEMPRE tratar os erros de forma específica é o ideal!


# Exemplo tratando erro de forma específica

try:
   geek() 
except  NameError:
    print('Esta função ainda não existe!')

"""

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except:
        return None


d = {'nome':'André'}
print(pega_valor(d, 'nome'))

