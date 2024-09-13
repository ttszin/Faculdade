#include<stdio.h>
#define MAX 100

int main(){

    double a[MAX],x;
    int i;
   
    for (i=0;i<MAX;i++){
        scanf("%lf",&a[i]);
        if (a[i]<=10){
            printf("A[%d] = %.1lf\n",i,a[i]);

        }


    }




    return 0;
}