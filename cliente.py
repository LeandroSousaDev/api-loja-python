from endereco import Endereco
from exceções import TipoInvalido
from produto import Produto


class Cliente:
    def __init__(self, nome, email, cidade, rua, numero):
        self.nome = nome
        self.email = email
        self.endereco = Endereco(cidade, rua, numero)
        self.carrinho_compras = []

    def adicionar_produto(self, novo_produto):
        if isinstance(novo_produto, Produto):
            self.carrinho_compras.append(novo_produto)
        else:
            raise TipoInvalido()

    def excluir_produto(self, produto):
        self.carrinho_compras.remove(produto)

    def valor_total(self):
        total = 0
        for produto in self.carrinho_compras:
            total += (produto.get_preco() * produto.get_quantidade())
        return total


    def exbir_carrinho(self):
        return [{
            "nome": produto.get_nome(),
            "preço": produto.get_preco(),
        } for produto in self.carrinho_compras]