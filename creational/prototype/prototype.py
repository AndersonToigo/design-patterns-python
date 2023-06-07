"""
Para exemplificar o uso do padrão Prototype, vamos imaginar que temos um sistema de gerenciamento de estoque de uma loja de roupas.
Nesse sistema, temos um objeto chamado `Produto` que possui os seguintes atributos:
- `nome`: Nome do produto.
- `preco`: Preço do produto.
- `quantidade`: Quantidade de produtos em estoque.

Temos também um objeto chamado `Estoque` que possui os seguintes atributos:
- `produtos`: Lista de produtos em estoque.

O nosso sistema possui uma funcionalidade que permite a criação de um novo produto, porém, para isso, o usuário deve informar o nome, o preço e a quantidade do produto.
Para isso, o sistema possui um formulário que o usuário deve preencher com essas informações.
Após o preenchimento do formulário, o sistema cria um novo produto com as informações informadas pelo usuário e adiciona esse produto ao estoque.

O problema é que, para cada produto que o usuário deseja criar, ele deve preencher o formulário novamente, o que pode ser um pouco cansativo.
Para resolver esse problema, podemos utilizar o padrão Prototype.
"""

from __future__ import annotations
from copy import deepcopy


class Product:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f'Produto: {self.name} | Preço: {self.price} | Quantidade: {self.quantity}'
    
    def clone(self) -> Product:
        return deepcopy(self)
    

class Inventory:
    def __init__(self) -> None:
        self.products = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def __str__(self) -> str:
        return '\n'.join([str(product) for product in self.products])
    

if __name__ == '__main__':
    inventory = Inventory()

    # Criando um produto
    product = Product('Camiseta', 50.0, 10)
    inventory.add_product(product)
    print(inventory)
    print()

    # Criando um novo produto a partir de um produto já existente
    new_product = product.clone()
    new_product.name = 'Calça'
    new_product.price = 100.0
    new_product.quantity = 5
    inventory.add_product(new_product)
    print(inventory)
    print()

    # Criando um novo produto a partir de um produto já existente
    new_product = product.clone()
    new_product.name = 'Boné'
    new_product.price = 20.0
    new_product.quantity = 20
    inventory.add_product(new_product)
    print(inventory)

