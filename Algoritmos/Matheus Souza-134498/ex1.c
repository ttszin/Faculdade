#include <stdio.h>

int main(){
	/*valimp e uma variavel para guardar o valor dos impostos*/
	int x,imposto,calculo,valimp,cont,vf;
	cont = 0;
	printf("Insira o valor para o calculo do imposto: ");
	scanf("%d",&x);
	while(x>=0){
		if(x<=190398){
			imposto = 0;
			calculo = 0;
			valimp = calculo;
		}
		if((x>190398)&(x<=282665)){
			imposto = 7.5;
			calculo = (x*imposto)/100;
			valimp = calculo;
		}
		if((x>282665)&(x<=375105)){
			imposto = 15;
			calculo = (x*imposto)/100;
			valimp = calculo;
		}
		if((x>375105)&(x<=466468)){
			imposto = 22.5;
			calculo = (x*imposto)/100;
			valimp = calculo;
		}
		if(x<=466468){
			imposto = 27.5;
			calculo = (x*imposto)/100;
			valimp = calculo;
		}
cont +=1;
if(cont==1){
	valimp = calculo;
}
if(cont>1){
	vf = valimp+valimp;
	
}






}
printf("o valor total arrecadado em imposto pelo governo e de: %f",vf);			
		
	
}
	



