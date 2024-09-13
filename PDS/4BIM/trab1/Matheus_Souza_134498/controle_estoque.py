from datetime import datetime

class Preco:
    def __init__(self, datainicial, datafinal, item, preco):
        self.datainicial = datetime.strptime(datainicial, "%Y-%m-%d")
        self.datafinal = datetime.strptime(datafinal, "%Y-%m-%d")
        self.item = item
        self.preco = preco

    def alocaItem(self):
        # Lógica para alocar um item ao preço
        if self.datainicial <= datetime.now() <= self.datafinal:
            print(f"Item {self.item.nome} alocado ao preço {self.preco}.")
        else:
            print(f"Período de validade do preço expirado.")

    def imprimePreco(self):
        print(f"Preço: {self.preco}, Válido de {self.datainicial} até {self.datafinal}")

    def inicializa(self):
        # Lógica de inicialização
        pass

    def localizaPreco(self, data):
        # Lógica para localizar o preço com base na data
        if self.datainicial <= data <= self.datafinal:
            return self.preco
        else:
            return None

class Produto:
    def __init__(self, codigo, nome, quantidade, unidade):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.unidade = unidade
        self.listaprecos = []

    def adicionaPreco(self, preco):
        self.listaprecos.append(preco)

    def devolucao(self, quantidade):
        # Lógica para processar a devolução
        self.quantidade += quantidade

    def executaBaixa(self, quantidade):
        # Lógica para executar a baixa de produtos
        if self.quantidade >= quantidade:
            self.quantidade -= quantidade
        else:
            print("Quantidade insuficiente em estoque.")

    def imprimeItem(self):
        print(f"Código: {self.codigo}, Nome: {self.nome}, Quantidade: {self.quantidade}")

    def inicializa(self):
        # Lógica de inicialização
        print("Item inicializado.")

    def imprimeProduto(self):
        print(f"Código: {self.codigo}, Nome: {self.nome}, Quantidade: {self.quantidade}")
        for preco in self.listaprecos:
            preco.imprimePreco()

    def removePreco(self, preco):
        self.listaprecos.remove(preco)

    def retornaCodigo(self):
        return self.codigo

    def verificaPreco(self):
        # Lógica para verificar o preço do produto
        if self.listaprecos:
            return self.listaprecos[0].preco
        else:
            return None

    def verificaProduto(self, codigo):
        return self.codigo == codigo

class Venda:
    def __init__(self, codigo, data, hora):
        self.codigo = codigo
        self.data = datetime.strptime(data, "%Y-%m-%d")
        self.hora = hora
        self.itensVenda = []

    def adicionaItem(self, item):
        self.itensVenda.append(item)

    def inicializa(self):
        # Lógica de inicialização
        self.itensVenda = []

    def imprimeVenda(self):
        print(f"Código: {self.codigo}, Data: {self.data}, Hora: {self.hora}")
        for item in self.itensVenda:
            item.imprimeItemVenda()

    def removeItemVenda(self, item):
        if item in self.itensVenda:
            self.itensVenda.remove(item)
            print("Item removido da venda com sucesso.")
        else:
            print("Item não encontrado na venda.")

class ItensVenda:
    def __init__(self, data, item, quantidade, venda):
        self.data = datetime.strptime(data, "%Y-%m-%d")
        self.item = item
        self.quantidade = quantidade
        self.venda = venda

    def alocaVenda(self):
        # Lógica para alocar uma venda
        print(f"Item associado à venda {self.venda.codigo}.")

    def devolveProduto(self):
        # Lógica para processar a devolução de um produto
        print(f"Produto devolvido da venda {self.venda.codigo}.")

    def inicializa(self):
        # Lógica de inicialização
        print("Item inicializado.")

    def localiza(self):
        # Lógica para localizar informações sobre o item de venda
        print(f"Informações sobre o item: {self.item.nome}, Quantidade: {self.quantidade}")

    def imprimeItemVenda(self):
        print(f"Data: {self.data}, Quantidade: {self.quantidade}")
        self.item.imprimeItem()

    def removeVenda(self):
        # Lógica para remover uma venda
        print(f"Venda {self.venda.codigo} removida do item.")

# Funções adicionadas com lógicas

# Lógica para adicionar um novo produto ao estoque
def adicionaProduto(estoque, produto):
    estoque.listadeprodutos.append(produto)
    print(f"Produto {produto.nome} adicionado ao estoque.")

# Lógica para adicionar uma nova venda ao estoque
def adicionaVenda(estoque, venda):
    estoque.listadevendas.append(venda)
    print(f"Venda {venda.codigo} adicionada ao estoque.")

# Lógica para consultar um produto no estoque
def consultaProduto(estoque, codigo):
    for produto in estoque.listadeprodutos:
        if produto.verificaProduto(codigo):
            return produto
    return None  # Retorna None se o produto não for encontrado

# Lógica para consultar uma venda no estoque
def consultaVenda(estoque, codigo):
    for venda in estoque.listadevendas:
        if venda.codigo == codigo:
            return venda
    return None  # Retorna None se a venda não for encontrada

# Lógica para imprimir todos os produtos no estoque
def imprimeProdutos(estoque):
    for produto in estoque.listadeprodutos:
        produto.imprimeProduto()

# Lógica para imprimir todas as vendas no estoque
def imprimeVendas(estoque):
    for venda in estoque.listadevendas:
        venda.imprimeVenda()

# Lógica para inicializar o estoque
def inicializaEstoque(estoque):
    estoque.listadeprodutos = []
    estoque.listadevendas = []
    print("Estoque inicializado.")

# Lógica para remover um produto do estoque
def removeProduto(estoque, codigo):
    produto = consultaProduto(estoque, codigo)
    if produto:
        estoque.listadeprodutos.remove(produto)
        print(f"Produto {produto.nome} removido do estoque.")
    else:
        print("Produto não encontrado no estoque.")

# Lógica para remover uma venda do estoque
def removeVenda(estoque, codigo):
    venda = consultaVenda(estoque, codigo)
    if venda:
        estoque.listadevendas.remove(venda)
        print(f"Venda {venda.codigo} removida do estoque.")
    else:
        print("Venda não encontrada no estoque.")

# Exemplo de uso:

# Criando um estoque
class Estoque:
    def __init__(self, empresa):
        self.empresa = empresa
        self.listadeprodutos = []
        self.listadevendas = []

estoque = Estoque(empresa="Minha Empresa")

# Inicializando o estoque
inicializaEstoque(estoque)

# Criando um produto
produto1 = Produto(codigo=1, nome="Produto A", quantidade=100, unidade="unidade")

# Adicionando um preço ao produto
preco1 = Preco(datainicial="2023-01-01", datafinal="2023-12-31", item=produto1, preco=10.0)
produto1.adicionaPreco(preco1)

# Adicionando o produto ao estoque
adicionaProduto(estoque, produto1)

# Imprimindo todos os produtos no estoque
imprimeProdutos(estoque)

# Criando uma venda
venda1 = Venda(codigo=1, data="2023-11-11", hora="14:30")

# Adicionando um item à venda
itemVenda1 = ItensVenda(data="2023-11-11", item=produto1, quantidade=5, venda=venda1)
venda1.adicionaItem(itemVenda1)

# Adicionando a venda ao estoque
adicionaVenda(estoque, venda1)

# Imprimindo todas as vendas no estoque
imprimeVendas(estoque)

# Removendo um produto do estoque
removeProduto(estoque, codigo=1)

# Removendo uma venda do estoque
removeVenda(estoque, codigo=1)
