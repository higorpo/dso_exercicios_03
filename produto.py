from categoria_produto import CategoriaProduto
from cliente import Cliente


class Produto:
    def __init__(self, codigo: int, descricao: str, categoria_produto: CategoriaProduto):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__quantidade = 0
        self.__preco_unitario = 0.0
        self.__cliente = None
        if isinstance(categoria_produto, CategoriaProduto):
            self.__categoria_produto = categoria_produto
        else:
            print('categoria_produto must be a instance of CategoriaProduto')

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @property
    def categoria_produto(self) -> CategoriaProduto:
        return self.__categoria_produto

    @categoria_produto.setter
    def categoria_produto(self, categoria_produto: CategoriaProduto):
        self.__categoria_produto = categoria_produto

    @property
    def quantidade(self) -> int:
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade: int):
        self.__quantidade = quantidade

    @property
    def preco_unitario(self) -> float:
        return self.__preco_unitario

    @preco_unitario.setter
    def preco_unitario(self, preco_unitario: float):
        self.__preco_unitario = preco_unitario

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        self.__cliente = cliente

    def preco_total(self) -> float:
        return self.__quantidade * self.__preco_unitario
