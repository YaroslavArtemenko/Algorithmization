#Контрольний приклад
##X = [0 1 2 3 4];
##Y = [0 1.18 1.9 2.33 2.59];


X = [0 1 2 3 4 5];
Y = [4.2 13.8 27.4 46.8 67.2 99.5];

n = length(X);

SumF = 0;
SumXt = 0;
SumXt2 = 0;
SumXF = 0;
SumY = 0;
SumA = 0;

for i=1:(n-1)
  F(i) = log((Y(i+1)-Y(i))/(X(i+1)-X(i)));
  SumF = SumF + F(i);
  
  Xt(i) = (X(i+1)+X(i))/2;
  SumXt = SumXt + Xt(i);

  Xt2(i) = (Xt(i))^2;
  SumXt2 = SumXt2 + Xt2(i);

  XF(i) = Xt(i)*F(i);
  SumXF = SumXF + XF(i);
end;


M = [(n-1) SumXt; SumXt SumXt2];
m = [SumF SumXF];

x = inv(M)*m';

disp('Коефіцієнти експоненціальної регресії:')
B = -x(2)
A = exp(x(1))/B

for i=1:n
  Yt(i) = A*(1-exp(-B*X(i)));
  SumY = SumY + (Y(i)-Yt(i));
end;

C = SumY/n
y = A*(1 - exp(-B*X)) + C;
%r = 0;

%Похибка апроксимації
for i=1:n
  SumA = SumA + abs((Y(i)-y(i))/Y(i));
  Ab(i) = abs((Y(i)-y(i))/Y(i));
%  if Ab(i) > r
%    r = Ab(i);
%    m = i
%  end;
end;
%r
%m
disp('Похибка(%):')
Abs = (SumA/(n-1))*100



wind3 = figure();
x = 0:0.1:5;
z = A*(1 - exp(-B*x)) + C;
l = polyfit(X, Y, (n-1));
y1 = polyval(l, x);

plot(X, Y, '^' ,x , z, 'm', x, y1, 'g')
xlabel('X');
ylabel('Y');
legend("margin - Своя, \ngreen - Встроенная");

grid on;


