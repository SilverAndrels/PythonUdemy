"""
Levantando os própios erros com raise

raise -> não é uma função. É uma palavra reservada como 'def' ou qualquer outra em Python.
raise é útil para que criarmos nossas próprias exceções e mensagens de erro.

Utilização geral é:
raise TipoDoErro('mensasgem de erro')

O raise finaliza a função assim como o return 
"""

# Exemplo


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'O texto "{texto}" será impresso na cor {cor}')


colore('André Silveira', 'Preto')

