from models.cardapio import Cardapio

cardapio = Cardapio('database/produtos.json')
cardapio.exibir()


def verifica_escolha(escolha):
    for produto in cardapio.produtos:
        if produto.nome == escolha:
            return True
    return False


roda_loop = True
while roda_loop:
    escolha = input('Escolha um produto pelo nome: ')
    if verifica_escolha(escolha):
        roda_loop = False
