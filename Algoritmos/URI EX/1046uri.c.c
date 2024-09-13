#include <stdio.h>
#include<string.h>

int main () {
	
	int i, t,duracao;
	
	printf("" "");
	scanf("%d",&i);
	scanf("%d",&t);
	duracao=t-i;	
	
	if (duracao<0) {
		duracao = 24+(t-i);
	
	}
	if (i==t) {
	
		printf("O JOGO DUROU 24 HORA(S)\n");
	}
	
	else printf("O JOGO DUROU %d HORA(S)\n", duracao);
	
}
		
	

	


