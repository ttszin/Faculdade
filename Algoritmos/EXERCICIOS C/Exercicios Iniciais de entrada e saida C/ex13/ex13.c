#include<stdio.h>

int main() {
	
	float r,c,d;
	
	printf("Insira a quantidade de dinheiro em reais: ");
	scanf("%f",&r);
	
	printf("Insira a taixa de conversao: ");
	scanf("%f", &c);
	
	d = r*c;
	
	printf("O valor em dolares e: %0.2f",d);
	
return 0 ;
	
	
}
