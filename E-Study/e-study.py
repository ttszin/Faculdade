#coding: UTF-8

from graphics import *
import time 
def main():
    win = GraphWin("E-STUDY",1050,700)
    bemvindo = Text(Point(525,150),"OLÁ, BEM VINDO AO E-STUDY!!!!\n FAÇA O LOGIN, SE AINDA NÃO ESTIVER SE REGISTRE!!!")
    bemvindo.setSize(20)
    bemvindo.draw(win)
    logintx = Text(Point(435,300),"LOGIN:")
    logintx.setSize(12)
    logintx.draw(win)
    entradalogin = Entry(Point(545,300),15)
    entradalogin.draw(win)
    login = entradalogin.getText()
    senhatx = Text(Point(435,350),"SENHA:")
    senhatx.setSize(12)
    senhatx.draw(win)
    entradasenha = Entry(Point(545,350),15)
    entradasenha.draw(win)    
    senha = entradasenha.getText()
    registrotx = Text(Point(555,370),"REGISTRE-SE")
    registrotx.draw(win)
    continua = Text(Point(685,325),"CONTINUAR")
    continua.setSize(12)
    continua.draw(win)
    
    clique = win.getMouse()
    x = clique.getX()
    y = clique.getY()
    print(x)
    print(y)
    
    def conferindo():
        dados = open("dadosdeusuarios.txt","r")
        
        info = dados.readlines()
        if login and senha in info:

            janela.close()
            principal = GraphWin("INÍCIO",1050,700)
        dados.close()
    
    if x>630 and x<740 and y>315 and y<340:
            login = entradalogin.getText()
            senha = entradasenha.getText()
    
        conferindo()


    
     
    if x>510 and x<600 and y>360 and y<381:
        win.close()
        janela = GraphWin("REGISTRE-SE",1050,700)
        registertxt = Text(Point(525,150),"REGISTRE-SE ABAIXO")
        registertxt.setSize(20)
        registertxt.draw(janela)    
        loginrtxt = Text(Point(400,300),"LOGIN DESEJADO:")
        loginrtxt.setSize(12)
        loginrtxt.draw(janela)
        entradaloginr = Entry(Point(545,300),15)
        entradaloginr.draw(janela)
        senhartx = Text(Point(400,350),"SENHA DESEJADA:")
        senhartx.setSize(12)
        senhartx.draw(janela)
        entradasenhar = Entry(Point(545,350),15)
        entradasenhar.draw(janela)
            
        
        
        dados = open("dadosdeusuarios.txt", "a+")
        
        
        confirma = Text(Point(685,330),"CONTINUAR")
        confirma.setSize(12)
        confirma.draw(janela)
        cliqueregistro = janela.getMouse()
        xr = cliqueregistro.getX()
        yr = cliqueregistro.getY()

        if xr>630 and xr<730 and yr>321 and yr<340:
            loginr = entradaloginr.getText()
            senhar = entradasenhar.getText()
            loginesenhanovos = (loginr+"\n",senhar+"\n")
            dados.write(str(loginesenhanovos))
    
        dados.close()    
        

    
            
        
main()

