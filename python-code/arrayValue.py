def calValue(a):
    sm = 0
    for i in range(1,len(n)):
        sm = sm + abs(a[i]-a[i-1])
    return sm

ln, nq = list(map(int, input().split()))
arr = list(map(int, input().split()))
val = calValue(arr)
