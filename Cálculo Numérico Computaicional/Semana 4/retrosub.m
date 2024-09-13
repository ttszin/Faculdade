%Função que resolve o sistema (busca a solução)

function x=retrosub(U,b) %início da função retrosubstituição
  n=length(b); %função que armazena o tamanho do vetor b
  x=zeros(n,1); %definindo a solução x como vetor coluna
  x(n)=b(n)/U(n,n); %isolando a incógnita x da última linha do sistema
  
  %ciclo de repetições de isolar todas as incógnitas x  
  for i=n-1:-1:1
    x(i)=( b(i)-U(i,i+1:n)*x(i+1:n) )/U(i,i);
  end
  
end %fim da function