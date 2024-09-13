#include <stdio.h>
#include <stdlib.h>
#define FALSE 0
#define TRUE 1

int main(){

    char cFrase[100], cPalavra[100];
    int palavraEncontrada = 0, j, i;
    int encontrei;

    printf("Digite uma palavra:");
    gets(cPalavra);

    printf("Digite uma frase:");
    gets(cFrase);

    j = -1;

    printf("%s\n", cPalavra);
    printf("%s\n", cFrase);

    for(i = 0; cFrase[i] != '\0'; i++)
    {
        j++;

        encontrei = FALSE;

        printf("Comparo %c(%d) com %c(%d)\n", cPalavra[j], j, cFrase[i], i);

            if(cPalavra[j] != cFrase[i])
            {
                j = -1;
                continue;
            }
            
            if(cPalavra[j+1] == '\0')
            {
                palavraEncontrada++;
                j = -1;	
                encontrei = TRUE;
            }

            if(cFrase[i+1] != cPalavra[0] && encontrei)
            {
            i--;
            }


    }

printf("A palavra aparece: %d vezes.\n", palavraEncontrada);

return 0;	
}