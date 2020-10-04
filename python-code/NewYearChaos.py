def minimumBribes(q):
    ln = len(q)
    index = [0] * ln
    b = True
    i = 0
    ct = ''
    while b and i < ln:
        index[q[i] - 1] = i
        if q[i] - i - 1 > 2:
            b = False
        i = i + 1
    if b:
        count = 0
        for i in range(ln, 0, -1):
            if index[i - 1] < i - 1:  # means that the element at q[i] needs to shift to the right
                k = index[i - 1]
                for j in range(k, min(k + 2, ln - 1)):
                    if q[j] > q[j + 1]:  # then swap elements
                        s = index[q[j] - 1]
                        index[q[j] - 1] = index[q[j + 1] - 1]
                        index[q[j + 1] - 1] = s
                        t = q[j]
                        q[j] = q[j + 1]
                        q[j + 1] = t
                        count += 1
        ct = str(count)
        # print(q)
    if not b:
        ct = 'Too chaotic'
    return ct


arr = [1, 2, 5, 3, 7, 8, 6, 4]

print(minimumBribes(arr))
