#include<stdio.h>
int main(){

    int m[LIN][COL];
    int i,j,k=0;

    for(i=0;i<LIN;i++){
        for(j=0;j<COL;j++){
            m[i][j]=k;
            k++;
        }
    }
    for(i=0;i<LIN;i++){
        for(j=0;j<COL;j++){
            printf("%d",m[i][j]);
        printf("\n";)
        }
    }
    printf("\n")
    for(j=0;j<COL;j++){
        for(i=0;i<LIN;i++){
            printf("%d",m[i][j]);
        printf("\n";)
        }
    }




    return 0;
}
