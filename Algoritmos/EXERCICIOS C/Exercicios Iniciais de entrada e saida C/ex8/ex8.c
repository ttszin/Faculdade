#include<stdio.h>

int main() {
	
	float x,y;
	int a = 14, b = 3;
	float z;
	x = a/b;
	y = a%b;
	z = y/x;
	
	printf("Valor de X: ");
	printf("%5.2f",x);
	
	printf("\nValor de Y: ");
	printf("%5.2f",y);
	
	printf("\nValor de Z: ");
	printf("%5.2f",z);
	
	return 0;
}

