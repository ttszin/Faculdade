#include<stdio.h>

int main() {
	
	int x,y,price;
	float pf;
	scanf("%d",&x);
	scanf("%d",&y);
	
	if (x==1){
		price=4;
		pf=price*y;
	}
		if (x==2){
		price=4.50;
		pf=price*y;
	}
		if (x==3){
		price=5.00;
		pf=price*y;
	}
		if (x==4){
		price=2.00;
		pf=price*y;
	}
		if (x==5){
		price=1.50;
		pf=price*y;
	}
	
	printf("Total: R$ %0.2f",pf);
	
	
	
	return 0;
	
}
