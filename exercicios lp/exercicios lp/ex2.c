#include<stdio.h>

int main(){

        double altura;
        int genero;

        printf("Insira sua altura: ");
        scanf("%lf",&altura);

        printf("Insira seu sexo: ");
        scanf("%d",&genero);

        if(genero == 0){
            int resp;
            resp = (73*altura)-58;
            printf("O seu peso ideal e de %d Kg",resp);

        }
        
        else if(genero ==1){
            int resp;
            resp = (62*altura)-45;
            printf("O seu peso ideal e de %d Kg",resp);

        }

    return 0;
}