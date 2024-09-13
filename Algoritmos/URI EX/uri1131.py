#coding:utf-8
import math


a = int(input(""))
b =int(input(""))
cont=1
inter=0
gremio=0
empates=0

if(a>b):
    inter+=1
elif(b>a):
    gremio+=1
elif(a==b):
    empates+=1

x = int(input("Novo grenal (1-sim 2-nao): "))

while(x==1):
    a = int(input(""))
    b =int(input(""))
    x = int(input("Novo grenal (1-sim 2-nao): "))
    if(a>b):
        inter+=1
    elif(b>a):
        gremio+=1
    elif(a==b):
        empates+=1
    cont+=1
else:
    
    if(x==2) and (inter>gremio) :
        print(cont," grenais")
        print("Inter: ", inter) 
        print("Gremio: ",gremio)
        print("Empates: ",empates)
        print("Inter venceu mais")
        

    elif(x==2) and (gremio>inter) :
        print(cont," grenais")
        print("Inter: ", inter) 
        print("Gremio: ",gremio)
        print("Empates: ",empates)
        print("Gremio venceu mais")
        
    
    elif(x==2) and (gremio==inter) :
        print(cont," grenais")
        print("Inter: ", inter) 
        print("Gremio: ",gremio)
        print("Empates: ",empates)
        print("Não houve vencedor")
        stop=True
    
    elif(x==2) and (gremio==inter) or (x==2) and (gremio==empates) or (x==2 )and(inter==empates):
        print(cont," grenais")
        print("Inter: ", inter) 
        print("Gremio: ",gremio)
        print("Empates: ",empates)
        print("Não houve vencedor")
        stop=True
    


    
