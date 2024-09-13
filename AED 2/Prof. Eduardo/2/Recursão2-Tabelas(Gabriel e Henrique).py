#coding: utf-8
#Gabriel Pedrosa - 132779
#Henrique Herrmmann - 134499

#ATENÇÃO: BUSCA LINEAR COM RECURSIVIDADE A PARTIR DA LINHA 35 À 47
#ATENÇÃO: BUSCA BINÁRIA COM RECURSIVIDADE A PARTIR DA LINHA 50 À 84

class Tabela_Contiguidade(object):
    def __init__(self, max_size):
        self.key = [None] * (max_size + 1)
        self.value = [None] * (max_size + 1)
        self.limit_i = 1
        self.limit_s = max_size
        self.start = self.limit_i - 1
        self.end = self.limit_s + 1
    
    def empty(self):
        return self.start < self.limit_i or self.end > self.limit_s
    
    def full(self):
        return (self.start == self.limit_i and self.end == self.limit_s)
    
    def get_size(self):
        if not(self.empty()):
            return self.end - self.start - 1
        else:
            return False
    
    def represent(self):
        table = ""
        if not(self.empty()):
            for i in range(self.start, self.end + 1):
                table += str(self.key[i]) + ": "+ str(self.value) + "\n"
        return table

    #Busca Linear Recursiva
    def search(self, key):
        newkey = -1
        if not(self.empty()):
            for i in range(self.start, self.end + 1):
                if(self.key[i] == key):
                    newkey = i
                    break 
                else:
                    newkey = -1
        else:
            newkey -1
        return newkey
    
    #Busca Binária
    def search_bin(self, value):
        self.middle = None
        newkey = -1
        if not(self.empty()):
            middle = self.end//2 + 1
            end = self.end
            newkey = self.recursive(middle, end, value)            
        else:
            newkey -1
        return newkey

    #Busca Binária Recursiva
    def recursive(self, middle, end, value):
        if(self.middle == middle):
            newkey = -1
            return newkey
        else:
            self.middle = middle
            if(self.value[middle] == value):
                return self.key[self.middle]
            elif(self.value[middle] > value):
                end = middle
                if(middle % 2 == 0):
                    middle = middle//2
                else:
                    middle = middle//2 + 1
                newkey = self.recursive(middle, end, value)
            elif(self.value[middle] < value):
                if((end+middle) % 2 == 0):
                    middle = (end+middle)//2
                else:
                    middle = (end+middle)//2 + 1
                newkey = self.recursive(middle, end, value)
            return newkey
    
    def show(self):
        print(self.end)
        for i in range(self.start, self.end +1):
            print("Pos: "+str(i)+" - Key:"+ str(self.key[i])+" - Value:"+ str(self.value[i]))

    def insert(self, key, value):
        position = self.search(key)
        if(position != -1):
            #self.key[position] = key
            self.value[position] = value
        elif not(self.full()):
            if(self.empty()):
                self.start = self.limit_i
                self.end = self.limit_i
            else:
                self.end += 1
            self.key[self.end] = key
            self.value[self.end] = value
    
    def insert_ord(self, key, value):
        position = self.search(key)
        if(position != -1):
            for i in range(self.end, self.start-1, -1):
                #print("End: "+str(i)+" "+str(self.value[i]))
                if(self.value[i] != None):
                    #print("Compar"+str(self.value[i]))
                    if(self.value[i] >= value):
                        self.key[i+1] = self.key[i]
                        self.value[i+1] = self.value[i]
                        self.key[i] = key
                        self.value[i] = value
                    else:
                        #print(self.value[i])
                        #print(value)
                        if(self.value[i] <= value):
                            self.key[i+1] = key
                            self.value[i+1] = value
                            break
        elif not(self.full()):
            if(self.empty()):
                self.start = self.limit_i
                self.end = self.limit_i
                self.key[self.end] = key
                self.value[self.end] = value
            else:
                #print("aqui")
                self.end += 1
                for i in range(self.end, self.start-1, -1):
                    #print("End: "+str(i)+" "+str(self.value[i]))
                    if(self.value[i] != None):
                        #print("Compar"+str(self.value[i]))
                        if(self.value[i] >= value):
                            self.key[i+1] = self.key[i]
                            self.value[i+1] = self.value[i]
                            self.key[i] = key
                            self.value[i] = value
                        else:
                            #print(self.value[i])
                            #print(value)
                            if(self.value[i] <= value):
                                self.key[i+1] = key
                                self.value[i+1] = value
                                break

    def consult(self, key):
        position = self.search(key)
        if position:
            return self.value[position]
        else:
            return False
    
    def delete(self, key):
        position = self.search(key)
        if position:
            for i in range(position, self.end):
                self.key[i] = self.key[i+1]
                self.value[i] = self.value[i+1]
            self.end -= 1
        else:
            return False
    
    def destroy(self):
        self.start = self.limit_i - 1
        self.end = self.limit_s + 1


#coding: utf-8

class Main(object):
    def __init__(self):
        print("Iniciando")
        menu = 1
        tam = int(input("Digite o tamanho da tabela: "))
        table = Tabela_Contiguidade(tam)
        while(menu != 0):
            menu = int(input("Opções:"
                +"\n1 - Inserir"
                +"\n2 - Mostrar"
                +"\n3 - Excluir"
                +"\n4 - Busca Linear"
                +"\n5 - Busca Binária"
                +"\n6 - Destruir"
                +"\n0 - Sair\n"))
            if(menu == 1):
                key = input("Digite a chave: ")
                value = int(input("Digite o valor: "))
                table.insert_ord(key, value)
                print("Valor Inserido")
            elif(menu == 2):
                table.show()
            elif(menu == 3):
                key = input("Digite a chave: ")
                if(table.delete(key)):
                    print("Valor deletado.")
                else:
                    print("Chave não encontrada.")
            elif(menu == 4):
                key = input("Digite a chave: ")
                resultado = table.search(key)
                if(resultado != -1):
                    print("A posição da chave digitada é:", resultado)
                else:
                    print("Chave não encontrada.")
            elif(menu == 5):
                value = int(input("Digite o valor: "))
                resultado = table.search_bin(value)
                if(resultado != -1):
                    print("A chave do valor digitado é:", resultado)
                else:
                    print("Valor não encontrado.")
            elif(menu == 6):
                table.destroy()
                print("Tabela Destruída. Saindo...")
                break


Main()