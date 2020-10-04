def maximumToys(prices,k):
    ln = len(prices)
    modp = []
    toycount = 0
    for i in range(0,ln):
        if prices[i] < k:
            toycount = toycount + 1 + maximumToys(prices[:i]+prices[(i+1):],k-prices[i])
    return toycount

sm = maximumToys([1,2,3,4,5],12)
print(sm)
