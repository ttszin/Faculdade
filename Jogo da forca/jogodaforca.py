#coding: UTF-8
import random
import time
from graphics import *
palavras = ["banana","goiaba","cadeira" ]
def main():
    
    janela=GraphWin("Jogo da Forca",1000,500)   #CRIAÇÃO DA JANELA
    #CRIAÇÃO DAS LINHAS DA FORCA
    base = Line(Point(50,450),Point(230,450)) 
    base.draw(janela)
    pilar = Line(Point(135,450),Point(135,70))
    pilar.draw(janela)
    linha3 = Line(Point(135,70),Point(300 ,70 ))
    linha3.draw(janela)
    linha4=Line(Point(300,70),Point(300,125))
    linha4.draw(janela)

    
    ##TEXTO DO JOGO DA FORCA 
    forca=Text(Point(650,50),"JOGO DA FORCA")
    forca.setSize(36)
    forca.draw(janela)

    ##TEXTO DE INICIO DO JOGO 
    inicio=Text(Point(650,95),"BEM VINDO AO JOGO, PRESSIONE A TECLA DE ESPAÇO PARA COMEÇAR!!!")
    inicio.setSize(12)
    inicio.draw(janela)
    key = janela.getKey()
    letraschutadas=[]
    chances=6
    acertou=0

    
    
    if key=="space": ## CHECANDO SE A TECLA ESPAÇO FOI PRESSIONADA
        inicio.undraw() ##TIRANDO A MENSAGEM DE INICIO 
        mensagem = Text(Point(650,350),"TENTE ADIVINHAR A PALAVRA!!\nVOCÊ TEM 6 TENTATIVAS\nDIGITE UMA LETRA NA CAIXA ABAIXO:") ## MOSTRANDO UMA NOVA MENSAGEM APÓ O INICIO DO JOGO 
        mensagem.setSize(14)
        mensagem.draw(janela)

        


        i=0
        elemento = random.choice(palavras)     ##PEGA UMA PALAVRA ALEATÓRIA DA LISTA
        elemento.replace("\n"," ")             
        i = len(elemento)                      ##QUANTAS LETRAS A PALAVRA TEM
        numletras=i
        

        quantletras=Text(Point(615,220),"A PALAVRA TEM {} LETRAS".format(numletras)) ## MOSTRANDO QUANTAS LETRAS TEM A PALAVRA ESCOLHIDA
        quantletras.setSize(13)
        quantletras.draw(janela)

        '''
        n=1
        if n==1:
            p1=300
            p2=350
            letras=Line(Point(p1,p2),Point(p2,p2))
            letras.draw(janela)
            cruzado=Line(Point(p1,p2),Point(p1,300))
            cruzado.draw(janela)
            n+=1
        while n>=2 and n<numletras:
            p1+=50
            p4=p1+100
            p3=p2-50 
            oletra=Line(Point(p1,p2),Point(p4,p2))
            oletra.draw(janela)
            cruzados = Line(Point(p1,p2),Point(p1,p3))
            cruzados.draw(janela)
            
            n+=1
        '''
        
        n=1
        p1=475
        p2=135
        letras=Circle(Point(p1,p2),22)     ## CRIA O PRIMEIRO CIRCULO PARA A PRIMEIRA LETRA 
        letras.draw(janela)
        n+=1
        while n>=2 and n<=numletras:
            p1+=50
            letras2=Circle(Point(p1,p2),22) ## CRIA OS OUTROS CIRCULOS PARA CADA LETRA
            letras2.draw(janela)
            n+=1
        
            entrada = Entry(Point(650,410),5) ##CRIA A CAIXA DE TEXTO PARA CHUTAR UMA LETRA
            entrada.draw(janela)
            chuteletra=entrada.getText()
            letraschutadas.append(chuteletra)
            
            if elemento =="goiaba":
                if chuteletra in elemento:
                    acerto=Text(Point(650,300),"VOCÊ ACERTOU UMA LETRA NA POSIÇÃO {}".format(elemento.index(chuteletra)))
                    acerto.setSize(12)
                    acerto.draw(janela)


        
        
        janela.getMouse()
    
    
    else:
        janela.close()     
    
    
    
        
main()                                                                