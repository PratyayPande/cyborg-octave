def minimumSwaps(arr):
    count = 0
    z = [0]*len(arr)
    dif = z
    srt = list(range(1,len(arr)+1))
    for x in range(len(arr)):
        dif[x] = (arr[x]-srt[x])
    while arr != srt:
        # find maximum and minimum elements in diff and their indexes
        minn = arr[0]
        maax = 0
        mx = 0
        mn = 0
        for i in range(0,len(dif)):
            if dif[i] > maax:
                maax = dif[i]
                mx = i
            if dif[i] < minn:
                minn = dif[i]
                mn = i
        # interchanging the elements
        print('array',end=': ')
        print(arr,end='')
        print('max indexed element',end=': ')
        print(arr[mx])
        print('min indexed element',end=': ')
        print(arr[mn])
        t = arr[mx]
        arr[mx] = arr[mn]
        arr[mn] = t
        count = count + 1
        # printing

        # modify dif now
        dif[mx] = arr[mx] - srt[mx]
        dif[mn] = arr[mn] - srt[mn]
    return count

arr = [7,1,3,2,4,5,6,9,8]
print(minimumSwaps(arr))
