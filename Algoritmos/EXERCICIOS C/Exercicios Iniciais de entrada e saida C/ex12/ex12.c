#include <stdio.h>

int main () {
	
	int y,r;
	float m;	
	printf("Insira o número de cartoes amarelos do jogador: ");
	scanf("%i", &y);
	
	printf("Insira o número de cartoes vermelhos do jogador: ");
	scanf("%i", &r);
	
	m = y*200+r*500;
	
	printf("O valor da multa que o jogador devera pagar e de: ");
	printf("%10.2f",m);
	printf("R$");	
	return 0;
	
}
