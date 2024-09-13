for i in range (0,100):
    nome= input("Nome: ")
    soma=0
    for n in range (0,4):
        nota=float(input("Nota "+str(n+1)+": "))
    soma=soma+nota
media=soma/4.0
print("   ---Nome:",nome," - Media",media)