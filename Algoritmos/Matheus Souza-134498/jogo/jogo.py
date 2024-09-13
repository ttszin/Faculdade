#coding: utf-8

from graphics import *
import math 
import time
import random


def main():
    win = GraphWin("Tiro ao alvo",800,600)
    win.setBackground("Red")
    gun = Image(Point(50, 300),"gun.png")
    gun.draw(win)
    alvo = Image(Point(700,300),"alvo1.png")
    alvo.draw(win)

    x=1
    while(x==1):
        x1 = random.randint(1, 20)
        alvo.move(0, x1)
        time.sleep(0.2)
        a1 = alvo.getAnchor().getY()
        if (a1>=500):
            alvo.move(0,x1*(-1))
        time.sleep(0)
            
            
            

main()
