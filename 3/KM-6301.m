h = 0.2
a = 2
b = 4
y0 = 1
y1 = -2
x0 = 2


function retval = second_der_func(x, y, y1)
 retval = -y + 2 * y1;
endfunction

x_list = cell(0, 11);
x_list(1) = x0;
y_res_list = cell(0, 11);
y_res_list(1) = y0;
y_derr = cell(0, 11);
y_derr(1) = y1;

x_axis = [x0];
y_axis = [y0];
y_derr_1 = [y1];

for i=1:10
  x_list(i+1) = x_list{i} + h;

  %rewritten from python Runge-Kutta alghorithm realization
  k0=h*y_derr{i};
  l0=h*second_der_func(x_list{i}, y_res_list{i}, y_derr{i});
  k1=h*(y_derr{i} + l0/2);
  l1=h*second_der_func(x_list{i}+h/2, y_res_list{i}+k0/2, y_derr{i});
  k2=h*(y_derr{i} + l1/2 - l0);
  l2=h*second_der_func(x_list{i}+h/2, y_res_list{i}+k1/2 - k0, y_derr{  i});

  y_res_list(i+1) = y_res_list{i} + 1/6 * (k0+4*k1+k2);
  y_derr(i+1) = y_derr{i} + 1/6 * (l0+4*l1+l2);
  
  %fill plot data matrixes
  x_axis = [x_axis; x_list{i+1}];
  y_axis = [y_axis, y_res_list{i+1}];
  y_derr_1 = [y_derr_1, y_derr{i+1}];
end;



disp('Власна функція:')
disp('    [a; b]:       y         z  ')
[x_axis(:) y_axis(:) y_derr_1(:)]  
  


function output = my_func(t, y)
  y;
  t;
  output = [y(2); 2*y(2) - y(1)];
endfunction

par=odeset ('InitialStep' ,h , 'MaxStep' ,h) ; 
[t_1, y_1] = ode45("@my_func", [a, b], [y0, y1], par);

disp('Вбудована функція:')
disp('    [a; b]:       y         z  ')
[t_1 y_1]

plot(x_axis, y_axis, "-o", t_1, y_1(:,1), "-o", x_axis, y_derr_1, "-o", t_1, y_1(:,2), "-o"), title('y');
legend("orange - Власна функція(y), \nblue -Вбудована функція(y), \nyellow - Власна функція(dy/dx), \npurple -Вбудована функція(dy/dx)");
grid on;

