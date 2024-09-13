%Função que permuta/troca as linhas

function [A,b]=troca_linhas(A,b,k,n)
 
 %calculo do valor máximo em módulo dos elementos "a" nas colunas (pivoteamento)
 [amax,i_max]=max(abs(A(k:n,k))) %i_max corresponde ao maximo dentro do vetor A(k+1:n,k)
 i_max=i_max+k-1; %acerta o indice que corresponde ao elemento maximo da matriz A na coluna k
 
 %verifica se o elemento "a" de valor máximo é muito pequeno
 if(amax <= eps)
              error('Eliminação Gaussiana não pode prosseguir: matriz A  singular.')
 end
 
%permutação dos elementos "a"
At=A(k,:); %linha de armazenamento temporario
A(k,:)=A(i_max,:);  %troca linha i por linha i_max
A(i_max,:)=At;  %troca linha i_max por linha i


%permutação dos elementos "b"
bt=b(k); %linha de armazenamento temporario
b(k)=b(i_max); %troca linha i por linha i_max
b(i_max)=bt; %troca linha i_max por linha i


%imprimi quais linhas foram trocadas
fprintf('Trocou-se a linha %i pela linha %i\n',k,i_max)

