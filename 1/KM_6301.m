A = [1 6 1; 3 7 12; 5 8 13; 7 9 14; 9 10 5];
b = [5 5 5 5 5];
[U, S, V] = svd(A);
X = V*diag([1/svd(A)(1), 1/svd(A)(2), 1/svd(A)(3)])*eye(3,5)*U'*b';
X

[P, d] = eig(A*A');
[K, e] = eig(A'*A);

S_new = eye(5,3);
for i=1:3
S_new(i,i) = sqrt(eig(A*A')(5-i+1));
end;

for i=1:5
  for j=1:5
  U_new(i,j) = -P(i,5-j+1);
end;
end;

for i=1:3
  V_new(i,1) = -K(i,3);
  V_new(i,2) = K(i,2);
  V_new(i,3) = K(i,1);
end;

X2 = V_new*diag([1/sqrt(eig(A*A'))(5),1/sqrt(eig(A*A'))(4), 1/sqrt(eig(A*A'))(3)])*eye(3,5)*U_new'*b';
X2