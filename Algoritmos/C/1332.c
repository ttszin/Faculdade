#include<stdio.h>
#include <string.h>
int main(){

    int n,i,cont;
    char palavra[10];
    scanf("%d",&n);
    for (i=1;i<=n;i++){
        scanf("%s",palavra);
        cont=0;
        if  (strlen(palavra)==5){
            printf("3\n");
        }

        else{
            if (palavra[0]=='o'){
                cont++;
            }    
            if (palavra[1]=='n'){
                cont++;
            }
            if (palavra[2]=='e'){
                cont++;
            }
            if (cont>=2){
                printf("1\n");
            }
        
            else {
                printf("2\n");
            }
        }
    }
    





    return 0;
}