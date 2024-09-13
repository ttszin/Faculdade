#include <stdio.h>

float soma(){
    float a,b,soma;
	soma = a+b;
    return soma;
}

float sub(){
	 float a,b,subtracao;
	printf("Digite o primeiro numero que quer subtrair: ");
    scanf("%f",&a);
    printf("Digite o segundo numero que quer subtrair: ");
    scanf("%f",&b);
    subtracao = a-b;
    printf("%.3f=",subtracao);
}

int fat(){
	
	
	
	
}


double fatorial(int x);
double fatorial(int x) {
double fat = 1;
int i;
for (i=x;i>1;i--)
fat=fat*i;
return fat;
}
	
int main(){
    int op,ini;
	scanf("%d",&ini);
	if (ini == 1)
	{
	printf("---- Menu ----- \n  0 - Sair \n  1 - Soma \n  2 - Subtracao \n  7 - Fatorial \n--------------- \n:");
	}
	scanf("%d",&op);
	if(op==1)
	{
    printf("Digite o primeiro numero que quer somar: ");
    scanf("%f",&a);
    printf("Digite o segundo numero que quer somar: ");
    scanf("%f",&b);
	soma();	
	}
	if(op==2)
	{
	sub();
	}
	if(op==7)
	{
	int n, p;
	double C;
	scanf("%d %d",&n, &p);
	if ((p>=0)&&(n>=0)&&(p<=n)){
	C= (fatorial(n) / (fatorial(p) * fatorial(n-p)));
	printf("%lf \n", C);
	} else {
	printf("Erro! Valor de n e/ou p invalido!! \n");
	}
	
	}
    

    return 0;

    



}
