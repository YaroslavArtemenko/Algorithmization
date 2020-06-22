%Варіант №7
disp('Вхідна матриця А та вектор b:')
A = [3 2 1; 1 12 2; 1 2 3; 4 2 1]
b = [3 2 1 3]
disp('Сингулярний розклад матриці:')
[U, S, V] = svd(A)
svd(A)
X = V*diag([1/svd(A)(1), 1/svd(A)(2), 1/svd(A)(3)])*eye(3,4)*U'*b';
disp('Вирішення перевизначеної системи:')
X
%Реалізація сингулярного розкладу
l = eig(A*A');
[L, d] = eig(A*A')
[M, e] = eig(A'*A)
S2 = eye(4,3);
S2(1,1) = sqrt(eig(A*A')(4));
S2(2,2) = sqrt(eig(A*A')(3));
S2(3,3) = sqrt(eig(A*A')(2));
for i=1:4
  U2(i,1) = -L(i,4);
  U2(i,2) = -L(i,3);
  U2(i,3) = L(i,2);
  U2(i,4) = L(i,1);
  end;
for i=1:3
  V2(i,1) = -M(i,3);
  V2(i,2) = M(i,2);
  V2(i,3) = M(i,1);
end;
X2 = V2*diag([1/sqrt(eig(A*A'))(4), 1/sqrt(eig(A*A'))(3), 1/sqrt(eig(A*A'))(2)])*eye(3,4)*U2'*b';
X2
%Перевірка
disp('Перевірка:')
r = A*X - b';
norm(r)
norm(r,2)
norm(r,1)
norm(r,inf)
norm(r,'fro')
disp('')
%Контрольний приклад
A = [1 6 1; 3 7 12; 5 8 13; 7 9 14; 9 10 5];
b = [5 5 5 5 5];
[U, S, V] = svd(A);
X = V*diag([1/svd(A)(1), 1/svd(A)(2), 1/svd(A)(3)])*eye(3,5)*U'*b';
disp('Контрольний приклад:')
X
