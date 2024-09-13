#include<stdio.h>

int main(){

    int num;
    printf("Digite um numero para saber se e primo: ");
    scanf("%d",&num);
    int i;
    int resultado;

    resultado = 0;
    for (i = 2; i <= num / 2; i++) {
        if (num % i == 0) {
        resultado++ ;
        break;
        }
    }
 
    if (resultado == 0){
        printf("%d e um numero primo\n", num);
    }
    else{
        printf("%d nao e um numero primo\n", num);
    
    
    }

    return 0;
}