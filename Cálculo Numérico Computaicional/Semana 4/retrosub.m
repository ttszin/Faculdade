%Fun��o que resolve o sistema (busca a solu��o)

function x=retrosub(U,b) %in�cio da fun��o retrosubstitui��o
  n=length(b); %fun��o que armazena o tamanho do vetor b
  x=zeros(n,1); %definindo a solu��o x como vetor coluna
  x(n)=b(n)/U(n,n); %isolando a inc�gnita x da �ltima linha do sistema
  
  %ciclo de repeti��es de isolar todas as inc�gnitas x  
  for i=n-1:-1:1
    x(i)=( b(i)-U(i,i+1:n)*x(i+1:n) )/U(i,i);
  end
  
end %fim da function