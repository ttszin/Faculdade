#coding: utf-8
#Gabriel Pedrosa - 132779
#Henrique Herrmmann - 134499

class Recursividade_1(object):
    def __init__(self):
        while True:
            print("-----Recursão 1-----")
            option = input("Selecione uma opção:"
            +"\n1 - Soma Elementos"
            +"\n2 - Fatorial"
            +"\n3 - Fibonacci"
            +"\n4 - Soma Digitos"
            +"\n0 - Sair\n")
            if(option == "1"):
                print("-------Somar Elementos-------")
                entrada = input("Digite os valores da listas separados por um espaço: ").split(" ")
                print(self.soma_elementos(entrada))
            elif(option == "2"):
                print("-------Fatorial-------")
                entrada = int(input("Digite um Número Natural:"))
                print(self.fatorial(entrada))
            elif(option == "3"):
                print("-------Fibonacci-------")
                entrada = int(input("Digite um Número Natural:"))
                print(self.fibonacci(entrada))
            elif(option == "4"):
                print("-------Somar Dígitos-------")
                entrada = input("Digite um Número:")
                print(self.soma_digitos(entrada))
            elif(option == "0"):
                break
            else:
                print("Opção Inválida.")


    def soma_elementos(self, lista):
        soma = 0
        if(len(lista) == 1):
            return int(lista[0])
        else:
            soma += int(lista.pop(-1))
            return soma + self.soma_elementos(lista)
    
    def fatorial(self, n):
        if(n == 1 or n == 0):
            return 1
        else:
            return n * self.fatorial(n - 1)        
    
    def fibonacci(self, n):
        if(n == 1 or n == 0):
            return 1
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)
    
    def soma_digitos(self, n):
        lista = list(n)
        
        return self.soma_elementos(lista)

Recursividade_1()
