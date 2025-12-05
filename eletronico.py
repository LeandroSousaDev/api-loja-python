from produto import Produto

class Eletronico(Produto):
    def __init__(self, nome, preco, estoque, imposto):
        super().__init__(nome, preco, estoque)
        self.__imposto = imposto

    def caucular_imposto(self):
        return super().caucular_imposto(self.__imposto)
    
    def descricao(self):
        return "descrição do produto"

televisao = Eletronico("tv-42", 1000, 10, 25)
print(televisao.descricao())