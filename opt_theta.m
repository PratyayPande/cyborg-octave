X = [[1,2104,5,1,45];[1,1416,3,2,40];[1,1534,3,2,30];[1,852,2,1,36]];
y = [460;232;315;178];
F = pinv(X'*X)*X'*y;
save hello.txt F -ascii;
save hello.mat F -ascii;
X = magic(15);
#imagesc(X),colorbar, colormap gray;
v = zeros(10,1);
for i = 1:10
  v(i) = 2^i;
endfor
imagesc(v),colorbar;