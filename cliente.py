from endereco import Endereco

class Cliente:
    def __init__(self, nome, email, cidade, rua, numero):
        self.nome = nome
        self.email = email
        self.endereco = Endereco(cidade, rua, numero)
        self.carrinho_compras = []

    def adicionar_produto(self, novo_produto):
        self.carrinho_compras.append(novo_produto)

    def exbir_carrinho(self):
        return [produto.nome for produto in self.carrinho_compras]