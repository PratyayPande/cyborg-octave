def hourglassSum(arr):
    row = len(arr)
    col = len(arr[0])
    mx = -9999
    # iterate rows from 0 to row-2
    for i in range(0,row-2):
        # iterate columns from 1 to col-1
        for j in range(1,col-1):
            s = arr[i][j-1]+arr[i][j]+arr[i][j-1] + arr[i+1][j] + arr[i+2][j]+arr[i+2][j-1]+arr[i+2][j+1]
            if s > mx:
                mx = s
    return mx


arr = [
