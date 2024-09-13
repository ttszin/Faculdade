%Função que transforma o sistema inicial em uma matriz triangular superior

function [A,b]=eli_gauss(A,b)  
  %dados de entrada (A,b) da função eli_gauss: matrizes A e b, do sistema Ax=b
  %dados de saida [A,b] da função eli_gauss: matrizes A e b modificadas, A na forma triangular superior
  
n=length(b); %função que armazena o tamanho do vetor b

pivotar=input('usar pivotação? sim=digite 1, não=digite 0     ') %decidir se usa ou não pivoteamento

%ciclo de repetições para percorrer todas as colunas da matriz A(i,j) 
 for k=1:n-1
  
    if ((pivotar==1) || abs(A(k,k))<= eps) %se sim para pivotear ou o valor absoluto dos elementos "a" são pequenos 
              pivo_old=A(k,k) %armazena pivô antigo
              [A,b]=troca_linhas(A,b,k,n);  %função troca de linhas
               pivo_new=A(k,k) %armazena pivô novo
    end
    
	  for i=k+1:n  %(j fixo) percorre todas as linhas i   
		    m=A(i,k)/A(k,k); %calculo do multiplicador
        fprintf('linha =%i, m=%f',k,m) %imprimi a coluna e o multiplicador
		    A(i,k)=0;  %zera coef da linha ij, j
        
        %Altera os elementos da matriz inicial para ficar zeros abaixo da diagonal principal
		    for j=k+1:n %(i fixo) percorre todas as colunas j
			    A(i,j)=A(i,j)-m*A(k,j);  %modifica os elementos "a" da matriz via operação elementar
		    end
		    b(i)= b(i)-m*b(k);  %modifica os elementos "b" da matriz via operação elementar
    end
    
    Ab=[A b] %armazena a nova matriz aumentada 
 end

 if(abs(A(n,n))<=eps) %verifica se o elemento "a" de valor máximo é muito pequeno
   disp('Warning: matriz A  singular. Retrosubstituição não poderá ser feita! ')
   pause %digite enter para finalizar
 end

end %fim da function



