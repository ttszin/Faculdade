#include<stdio.h>

int main(){
	
	int i,num[10],x ;
	for (i = 0;i<10; i++){
		printf("Digite o %d numero\n ",i+1);
		scanf("%d", &num[i]);
	}
	for(x = i-1;x>=0;x--){
		printf("num[%d] = %d\n",x ,num[x]);
	}
		
	return 0;	
	
	
	
	
	
}
