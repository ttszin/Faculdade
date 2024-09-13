#include<stdio.h>

int main(){

    char  frase1[101],frase2[101],frase3[101];

        scanf(" %[^\n]s", frase1);
        scanf(" %[^\n]s", frase2);
        scanf(" %[^\n]s", frase3);

    printf("%s%s%s\n",frase1,frase2,frase3);
    printf("%s%s%s\n",frase2,frase3,frase1);    
    printf("%s%s%s\n",frase3,frase1,frase2);
    printf("%.10s%.10s%.10s\n",frase1,frase2,frase3);
    
    return 0;
}