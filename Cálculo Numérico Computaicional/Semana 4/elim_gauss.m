
%Determinando o sistema linear

A=[2 2 1 1;
   1 -1 2 -1;
   3 2 -3 -2;
   4 3 2 1]
   
b=[7; 1;4;12]


   [U,b2]=eli_gauss(A,b) %fun��o que triangulariza o sistema  
  
   x=retrosub(U,b2) %fun��o que resolve o sistema 
   
   C=x(1) , A=x(2), Da=x(3), Dv=x(4) %imprimi a solu��o
   
   b5=C+A+2*Da+2*Dv