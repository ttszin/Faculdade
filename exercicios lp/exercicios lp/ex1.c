#include <stdio.h>


int main(){


    float fahrenheit;
    float resp;
    
    printf("Digite a temperatura que deve ser convertida: ");
    scanf("%f",&fahrenheit);

    resp = ((fahrenheit-32)*5)/9;

    printf("A temperatura %f em graus Fahrenheit, sera %.2f graus Celsius", fahrenheit,resp);

    return(0);
}