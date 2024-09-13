#include<stdio.h>
#include<string.h>

int main(){
	
	int a,b,x,inter,gremio,empates,cont;

	scanf("%d",&a);
	scanf("%d ",&b);
	cont=1;
	inter=0;
	gremio=0;
	empates=0;
	printf("Novo grenal (1-sim 2-nao): ");
	scanf("%d",&x);

	if(a>b){
	    inter+=1;
	}
	if(b>a){
	    gremio+=1;
	}
		
	if(a==b){
	    empates+=1;
	}
	
	
	while(x==1){
	    scanf("%d",&a);
		scanf("%d ",&b);
	    printf("Novo grenal (1-sim 2-nao): ");
		scanf("%d",&x);
	    if(a>b){
	        inter+=1;
		}
	    if(b>a){
	        gremio+=1;
		}
	    if(a==b){
	        empates+=1;
	    cont+=1;
		}
	}
	

		
	print(cont," grenais");
	print("Inter: ", inter);
	print("Gremio: ",gremio);
	print("Empates: ",empates);
	print("Não houve vencedor");

return 0;	    
}	






    

