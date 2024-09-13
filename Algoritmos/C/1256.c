#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#define N 100

void imprimiHash(TNo *inicio, int ind){
	TNo *aux = inicio;
	printf("%d -> ", ind);
	while(aux != NULL){
		printf("%d -> ", aux->valor);
		aux = aux->prox;
	}		
	printf("\\");
	printf("\n");
}

void insereNo(TDes *vetor, int ind, int e){
	TNo *aux = (TNo *)malloc(sizeof(TNo));
	aux->valor = e;
	aux->prox = NULL;
	if(vetor[ind].inicio == NULL)
		vetor[ind].inicio = aux;
	else
		vetor[ind].final->prox = aux;
	vetor[ind].final = aux;
}

void inicializa(TDes *vetor, int n){
	int i;
	for(i=0; i<n; i++){
		vetor[i].inicio = NULL;
		vetor[i].final = NULL;
	}
}


int main(){
    int n,i;
    scanf("%d",&n);
    for(i=0;i<n;i++)[

    ]




    return 0;
}