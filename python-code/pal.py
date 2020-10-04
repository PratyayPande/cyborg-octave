def checkPal(s):
    return s == ''.join(reversed(s))

q = int(input(''))
sols = []
for i in range(0,q):
    sp = str(input(''))
    h = 0
    nm = sp
    while checkPal(nm) == False and h < len(sp):
        nm = sp[:h] + sp[h+1:]
        h = h + 1
        print(h)
        print(sp[:h] + sp[h+1:])
    sols.append(h-1)
print(sols)
