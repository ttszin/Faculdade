function [x,k]=gaussjac(a,b,p)
  n=max(size(a));
  k=0;
  for i=1:n
    x0(i)=0.5;   %x0=[2.5; -0.5; 0;0];
    s=0;
    for j=1:n
      if j~=i
        s=s+abs(a(i,j));
      end
    end
    alf(i)=s/abs(a(i,i));
  end
  if max(alf)<1 %teste convergência
    teste=1000;
    while teste>p %critério de parada
      k=k+1;
      for i=1:n
        s=0;
        for j=1:n
          if j~=i
            s=s+a(i,j)*x0(j);
          end
        end
        x(i)=(b(i)-s)/a(i,i); %cálculo das soluções x
      end
      teste=max(abs(x-x0));
      x0=x;
    end
    x=x';
  else
    x= 'não converge';
  end
  
  
