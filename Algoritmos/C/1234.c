#include<stdio.h>
#include <ctype.h>
int main(){

    int i;
    char frase[100];
   
    scanf("%s",frase);
    printf("%s",frase);
    for(i=0;i<strlen(frase);i++){
        for(i=0;i<strlen(frase);i++){
            frase[i]=toupper(frase[i]);
            i++;
        }

        for(i=1;i<strlen(frase);i++){
            frase[i]=tolower(frase[i]);
            i++;
        }
    }
    printf("%s",frase);




    return 0;
}