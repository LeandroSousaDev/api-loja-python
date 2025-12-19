from categoria import Eletronico, Alimento, Roupas
from cliente import Cliente
from exceções import TipoInvalido, ProdutoIndisponivel, ErroNoValor

try:
    televisao = Eletronico("tv42 sansung", 1000, 10, 1, 10)
    hamburger = Alimento("Xburger", 20, 10, 5, 10)
    marcos = Cliente("Marcos", "marcos@email.com", "Salvador", "rua", 30)

    marcos.adicionar_produto(televisao)
    marcos.adicionar_produto(hamburger)

    print({
        "cliente": marcos.nome,
        "carrinho": marcos.exbir_carrinho(),
        "total": marcos.valor_total()
    })

except TipoInvalido as erro:
    print(erro)

except ProdutoIndisponivel as erro:
    print(erro)

except ErroNoValor as erro:
    print(erro)


