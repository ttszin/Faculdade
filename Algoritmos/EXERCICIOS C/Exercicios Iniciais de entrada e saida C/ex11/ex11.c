#include<stdio.h>

int main() {
	
	
	float d, t;
	float v;
	
	
	printf("Determine a distância percorida (em km): ");
	scanf("%f",& d);
	
	printf("Determine o tempo (em horas): ");
	scanf("%f",& t);
	
	v=d/t;
	
	printf("A velocidade do maratonista e: ");
	printf("%5.2f",v);
	printf(" km/h");
	
	return 0;
	
}
