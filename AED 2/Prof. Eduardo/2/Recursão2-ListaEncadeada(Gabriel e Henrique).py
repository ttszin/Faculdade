#coding: utf-8

#Gabriel Pedrosa - 132779
#Henrique Herrmmann - 134499

#ATENÇÃO: BUSCA COM RECURSIVIDADE A PARTIR DA LINHA 73
class Produto(object):
    def __init__(self):
        print("Inicilizando...")
        
    def criar(self, size):
        print("Criando Lista...")
        self.size = size
        self.list = [None]*size
        self.increase = 0
        print(("Criado"))

    def inserir(self, position, produto):
        if(self.size > self.increase):
            print("Inserindo Produto...")
            allow = True
            other = False
            if(self.list[position] != None ):
                sure = int(input("Já existe um produto nessa posição.\nDeseja Sobreescrever: 1 - Sim, 2 - Não\n"))
                if(sure == 1):
                    allow = True
                else:
                    sure2 = int(input("Deseja inserir na proxima posição: 1 - Sim, 2 - Não\n"))
                    if(sure2 == 1):
                        cont = position
                        for i in self.list:
                            if(cont >= self.size):
                                cont = 0
                            if(i == None):
                                next = cont
                                break
                            cont += 1
                        self.inserir(next, produto)
                        allow = True
                        other = True
                    else:
                        allow = False
            if allow and not(other):
                self.list[position] = produto
                print("Inserido")
                self.increase += 1
            elif not(allow) and not(other):
                print("Não inserido")
        else:
            print("Lista Cheia!")

    def remover(self, position):
        print("Removendo Produto...")
        self.list[position] = None
        print("Removido")
    
    def retornar(self, produto):
        print("Retornar Nome do Produto...")
        cont = 0
        for i in self.list:
            if(i == produto):
                print("Posição: "+str(cont)+" Produto: "+str(i))
            cont += 1
    
    def buscar(self, produto):
        print("Buscar posição do Produto")
        cont = 0
        for i in self.list:
            if(i == produto):
                print("Posição: "+str(cont))
            cont += 1
    
    #Busca com RECURSÃO
    def buscar_recursiva(self, produto, tamanho):
        if(tamanho == 0):
            print("Nenhum Produto Encontrado!")
        else:
            if(produto == self.list[tamanho-1]):
                print("Registro: "+str(tamanho - 1)+" - "+str(self.list[tamanho-1]))
            else:
                tamanho -= 1
                self.buscar_recursiva(produto, tamanho)
                
    
    def imprimir(self):
        print("Imprimindo valor...")
        cont = 0
        for i in self.list:
            if (i != None):
                print(cont, i)
            else:
                print(cont, " ")
            cont += 1
        print("Impresso")
        
class main(object):
    def __init__(self):
        p = Produto()
        continuar = True
        while(continuar):
            menu = int(input("Escolha uma opção!\n 1 - Criar a lista\n 2 - Inserir um produto\n 3 - Remover um produto\n 4 - Retornar um produto\n 5 - Buscar um produto\n 6 - Imprimir a Lista\n 7 - Sair\n"))
            if(menu == 1):
                size = int(input("Informe o tamanho da lista:\n"))
                p.criar(size)
            elif(menu == 2):
                position = int(input("Informe a posição do produto que deseja inserir na lista :\n"))
                produto = input("Informe o nome do produto:\n")
                p.inserir(position, produto)
            elif(menu == 3):
                position = int(input("Informe a posição do produto que deseja remover da lista :\n"))
                p.remover(position) 
            elif(menu == 4):
                produto = input("Informe o nome do produto que deseja encontrar:\n")
                p.retornar(produto) 
            elif(menu == 5):
                produto = input("Informe o nome do produto que deseja buscar:\n")
                p.buscar_recursiva(produto, size)
            elif(menu == 6):
                p.imprimir()
            elif(menu == 7):
                continuar = False 

main()