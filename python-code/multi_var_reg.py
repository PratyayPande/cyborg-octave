import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# code to perform gradient descent

dataset = pd.read_excel('test_dataset.xls')
X = dataset.iloc[:, 1:].values
y = dataset.iloc[:, 0].values
nX = np.array(X)
nY = np.array(y)
# print('end ',nX[3])
print('completed importing the dataset')
row, col = np.shape(nX)
on = np.ones((row,1), dtype=float)
nX = np.hstack((on, nX))
col = col + 1
theta = np.ones((col,1), dtype=float)
# theta[col-1] = 1
newtheta = np.ones((col,1), dtype=float)
print('completed initialising the matrices')
alpha = 0.0000445 # not the optimum value of alpha - have to make changes
tol = 0.0001
niter = 1
prev = 1
J = 0
num = 10000 # value converges to |dJ| = 0.2 10 0.3 after 8000 iterations
arrJ = np.zeros((num,1),dtype=float)
ind = list(range(0,num))
# 1 iteration of gradient descent
while((abs(J-prev) > tol) and (niter < num)):
    prev = J
    newtheta = theta
    J = 0
    for i in range(0, len(theta)):
        sum = 0.0
        # calculation of summation of derivative
        for r in range(0, row):
            # calculation of h(x)
            h = 0.0
            for g in range(0, col):
                h = h + (nX[r][g] * theta[g])
            # calculated h
            sum = sum + (h - y[r]) * nX[r][i]
            J = J + (h - y[r])*(h - y[r])
        #print('value of derivative = %f'%((alpha/row)*sum))
        newtheta[i] = newtheta[i] - (alpha / row) * sum
    J = J/(2*row)
    '''
    print('value of theta for iteration no. = %d'%niter)
    for i in range(1, len(theta) - 1):
        print(theta[i])
    '''
    theta = newtheta
    '''
    print('value of newtheta for iteration no. = %d' % niter)
    for i in range(1, len(theta) - 1):
        print(theta[i])
    '''
    print('J = %0.7f'%J, end=', ')
    #print('prev = %0.7f'%prev, end=', ')
    arrJ[niter - 1] = J
    niter = niter + 1
    print('niter = %d'%niter)
print("final value of theta")
plt.plot(ind,arrJ)
plt.xlabel('Number of iterations')
plt.ylabel('Cost Function')
plt.grid
plt.show()
for i in range(1,len(theta)-1):
    print(theta[i])

# end of
