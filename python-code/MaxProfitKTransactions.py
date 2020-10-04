# bad algorithm for practice: exponential complexity
def maxProfitWithKTransactions(prices, k):
    mx = 0
    nm = 0
    for i in range(0, len(prices) - 2 * (k - 1) - 1):
        for j in range(i + 1, len(prices) - 2 * (k - 1)):
            #print('prices', end=' = ')
            #print(prices, end=', k = ')
            #print(k, end=', i = ')
            #print(i, end=', j = ')
            #print(j, end=', mx = ')
            #print(mx)
            if k > 1:
                nm = maxProfitWithKTransactions(prices[j + 1:], k - 1)
            mx = max(mx, nm + prices[j] - prices[i])
    return mx


arr = [5, 11, 3, 50, 60, 90, 1, 91]
nTransactions = 3
print(maxProfitWithKTransactions(arr, nTransactions))
