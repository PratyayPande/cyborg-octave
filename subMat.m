function mat = subMat(X,theta,y)
  m = length(y);
  alpha = 0.1;
  sgm = (alpha/m)*(X*theta - y);
  for i = 1:length(y)
    theta(i) = theta(i) - sum(sgm.*X(:,i));
  endfor
endfunction
