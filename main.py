from categoria import Eletronico, Alimento, Roupas
from cliente import Cliente

televisao = Eletronico("tv42 sansung", 1000, 1, 10)
hamburger = Alimento("Xburger", 20, 3, 5)
marcos = Cliente("Marcos", "marcos@email.com", "Salvador", "rua 1", 30)

marcos.adicionar_produto(televisao)
marcos.adicionar_produto(hamburger)

print([produto.get_nome() for produto in marcos.carrinho_compras])

for produto in marcos.carrinho_compras:
    print(produto.get_nome())