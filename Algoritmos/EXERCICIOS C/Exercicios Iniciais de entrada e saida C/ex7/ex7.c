#include<stdio.h>
int main() {
int x,y,z;
x=y=10;
z=x;
x++;
x=--x;
y++;
x=x+y-((z)*10);

printf("Valor de X: ");
printf("%i", x);

printf("\nValor de Y: ");
printf("%i",y);

printf("\nValor de Z: ");
printf("%i", z);



return 0;


}

