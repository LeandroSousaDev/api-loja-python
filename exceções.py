class TipoInvalido(Exception):
    def __init__(self):
        super().__init__("Voce deve adicionar um produto ao carrinho do cliente")

class ErroNoValor(Exception):
    def __init__(self, variavel):
        super().__init__(f"Valor de {variavel} não dever ser negativo")

class ProdutoIndisponivel(Exception):
    def __init__(self, produto):
        super().__init__(f"produto {produto} em estoque é insuficiente")