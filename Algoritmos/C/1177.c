#include<stdio.h>

int main(){

    int t,i,cont;
    int n[1000];
    scanf ("%d", &t);
    cont=0;
    if (t>=2 && t<=50){
        for(i=0;i<1000;i++){
            printf("N[%d] = %d\n",i,cont);
            cont++;
            if (cont==t){
                cont=0;
            }
        }

    }





    return 0;
}