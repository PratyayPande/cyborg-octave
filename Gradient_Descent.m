% This one works!! Need to clarify on the initial value of theta
A = [1 2 4;3 4 5;4 6 7];
m = size(A)(1);
A = [ones(m,1) A];
theta = [0;0;0;1];
y = [6;3;1];
E = 0.00001; % tolerance value
del = 1; % for storing the difference
prevJ = 0;
J = 0;
alpha = 0.001;
printf('Test, J = ');
niter = 0;
while(del > E)
    prevJ = J;
    niter = niter + 1;
    J = (alpha/2*m)*sum((A*theta - y).^2);
    del = abs(prevJ - J);
    theta = theta - (alpha/m)*(A'*(A*theta - y));
end
disp(J);
disp(theta);
printf('niter = %d\n',niter);
printf("End of file\n");
