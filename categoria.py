from produto import Produto

class Eletronico(Produto):
    def __init__(self, nome, preco, quantidade, desconto):
        super().__init__(nome, preco, quantidade)
        self.__desconto = desconto
        self.__categoria = "Eletronico"

    def caucular_desconto(self):
        return super().caucular_desconto(self.__desconto)
    
    def descricao(self):
        return "descrição do eletronico"
    
class Roupas(Produto):
    def __init__(self, nome, preco, quantidade, desconto):
         super().__init__(nome, preco, quantidade)
         self.__desconto = desconto
         self.__categoria = "Roupa"

    def caucular_desconto(self):
        return super().caucular_desconto(self.__desconto)
    
    def descricao(self):
        return "descrição da roupa"
    
class Alimento(Produto):
    def __init__(self, nome, preco, quantidade, desconto):
         super().__init__(nome, preco, quantidade)
         self.__desconto = desconto
         self.__categoria = "Alimento"

    def caucular_desconto(self):
        return super().caucular_desconto(self.__desconto)
    
    def descricao(self):
        return "descrição do alimento"
    

