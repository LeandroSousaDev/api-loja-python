from exceções import TipoInvalido, ProdutoIndisponivel, ErroNoValor
from produto import Produto

class Eletronico(Produto):
    def __init__(self, nome, preco, estoque, quantidade, desconto):
        super().__init__(nome, preco, estoque)
        if desconto < 0:
            raise ErroNoValor("desconto")
        self.__desconto = desconto
        if quantidade < 0:
            raise ErroNoValor("quantidade")
        self.__quantidade = quantidade

        if quantidade > estoque:
            raise ProdutoIndisponivel(self.get_nome())

        self.__categoria = "Eletronico"

    def get_desconto(self):
        return self.__desconto

    def get_quantidade(self):
        return self.__quantidade

    def get_quantidade(self):
        return self.__quantidade

    def adicionnar_desconto(self):
        self.set_preco(self.get_preco() - self.__desconto)
    
    def descricao(self):
        return {
            "nome": self.get_nome(),
            "preco": self.get_preco(),
            "estoque": self.get_estoque(),
            "quantidade": self.get_quantidade(),
            "desconto": self.get_desconto(),
            "categoria": self.get_quantidade()
        }
    
class Roupas(Produto):
    def __init__(self, nome, preco, estoque, quantidade, desconto):
        super().__init__(nome, preco, estoque)
        if desconto < 0:
            raise ErroNoValor("desconto")
        self.__desconto = desconto
        if quantidade < 0:
            raise ErroNoValor("quantidade")
        self.__quantidade = quantidade

        if quantidade > estoque:
            raise ProdutoIndisponivel(self.get_nome())

        self.__categoria = "Roupa"

    def get_desconto(self):
        return self.__desconto

    def get_quantidade(self):
        return self.__quantidade

    def get_quantidade(self):
        return self.__quantidade


    def adicionar_desconto(self):
        self.set_preco(self.get_preco() - self.__desconto)
    
    def descricao(self):
        return {
            "nome": self.get_nome(),
            "preco": self.get_preco(),
            "estoque": self.get_estoque(),
            "quantidade": self.get_quantidade(),
            "desconto": self.get_desconto(),
            "categoria": self.get_quantidade()
        }
    
class Alimento(Produto):
    def __init__(self, nome, preco, estoque, quantidade, desconto):
        super().__init__(nome, preco, estoque)
        if desconto < 0:
            raise ErroNoValor("desconto")
        self.__desconto = desconto
        if quantidade < 0:
            raise ErroNoValor("quantidade")
        self.__quantidade = quantidade

        if quantidade > estoque:
            raise ProdutoIndisponivel(self.get_nome())

        self.__categoria = "Alimento"

    def get_desconto(self):
        return self.__desconto

    def get_quantidade(self):
        return self.__quantidade

    def get_quantidade(self):
        return self.__quantidade

    def adicionar_desconto(self):
        return self.set_preco(self.get_preco() - self.__desconto)
    
    def descricao(self):
        return {
            "nome": self.get_nome(),
            "preco": self.get_preco(),
            "estoque": self.get_estoque(),
            "quantidade": self.get_quantidade(),
            "desconto": self.get_desconto(),
            "categoria": self.get_quantidade()
        }
