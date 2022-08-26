import json


class Produto():

    def __init__(self, nome_parametro, preco_parametro):
        self.nome = nome_parametro
        self.preco = preco_parametro


class Cardapio():
    
    def __init__(self, arquivo_produtos):
        self.produtos = self.__carregar_produtos(arquivo_produtos)

    def __carregar_produtos(self, arquivo):
        arquivo = open(arquivo)
        dados = json.load(arquivo)
        arquivo.close()

        produtos = []
        for lanche in dados['lanches']:
            nome = list(lanche.keys())[0]
            preco = list(lanche.values())[0]
            produto = Produto(nome, preco)
            produtos.append(produto)

        return produtos

    def exibir(self):
        print('Cardápio:')
        indice = 1
        for produto in self.produtos:
            print(f'\t{indice} - {produto.nome} R$ {produto.preco:.2f}')
            indice = indice + 1

class Pedido():
    pass