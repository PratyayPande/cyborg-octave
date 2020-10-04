h = [9, 7, 4, 2, 7]
ncount = len(h)
for i in range(0, ncount - 1):
    for j in range(i + 1, ncount):
        print('%d' % h[i], end=', ')
        print('%d' % h[j])
