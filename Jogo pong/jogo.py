#coding:UTF-8
from graphics import *
import time
import math
end = False
janela = GraphWin("PONGO",800,600) 
recado = Text(Point(400,280),"PRESSIONE QUALQUER TECLA PARA COMEÇAR O JOGO")
recado.setSize(15)
recado.draw(janela)
checkinicio = janela.getKey()
recado.undraw()
player = Rectangle(Point(40,230),Point(70,370))
player.setWidth(3)
player.setFill("black")
player.setOutline("red")
player.draw(janela)
player2 = Rectangle(Point(730,230),Point(760,370))
player2.setWidth(3)
player2.setFill("black")
player2.setOutline("blue")
player2.draw(janela)


bola = Circle(Point(400,300),40)
bola.setFill("yellow")
bola.draw(janela)

right = True
cima =  True
janela.ligar_Buffer()

while end!=True:
    
    if player.getCenter() == bola.getCenter().getX()-40:
        right = True
    
    if bola.getCenter().getX()+40>=725 :
        right = False
    #if bola.getCenter().getX()-40<=72:
        #right = True
    if right == True:
        bola.move(10,0)
    else:
        bola.move(-10,0)


    if bola.getCenter().getY()+40>=600 :
        cima = False
    if bola.getCenter().getY()-40<=5:
        cima = True
    if cima == True:
        bola.move(0,10)
    else:
        bola.move(0,-10)

    tecla1 = janela.checkKey_Buffer()
    update()
    
    
    if len(tecla1)>0 and "Up" in tecla1:
        player2.move(0,-20)
    if len(tecla1)>0 and "Down" in tecla1:
        player2.move(0,20)
    

    if len(tecla1)>0 and "w" in tecla1:
        player.move(0,-20)
    if len(tecla1)>0 and "s" in tecla1:
        player.move(0,20)
    time.sleep(0.1)

      
    
   

  
    
    
    
    
    
    





        
        


    