X = [1,2,3,4;5,6,7,8;6,3,2,4;7,9,1,3];
y = [7,1,5,8];
m = size(X)(1);
X = [ones(m,1),X]
k = X'*X
a = inv(k)
b = a*X'
theta = b*y';
printf("The value of theta = \n");
disp(theta);
