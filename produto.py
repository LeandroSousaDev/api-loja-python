from exceções import ErroNoValor


class Produto:
    def __init__(self, nome, preco, estoque):

        self.__nome = nome
        if preco < 0:
            raise ErroNoValor("preço")
        self.__preco = preco
        if estoque < 0:
            raise ErroNoValor("estoque")
        self.__estoque = estoque

    def get_nome(self):
        return self.__nome
    
    def set_preco(self, novo_nome):
        self.__nome = novo_nome

    def get_preco(self):
        return self.__preco
    
    def set_preco(self, novo_preco):
        self.__preco = novo_preco

    def get_estoque(self):
        return self.__estoque

    def set_estoque(self, novo_estoque):
        self.__estoque = novo_estoque

    def descricao(self):
        return "descrição generica"