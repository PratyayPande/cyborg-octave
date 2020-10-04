import math

n = list(map(int, input('').split(' ')))
s1 = math.ceil(n[0]/n[2])
s2 = math.ceil(n[1]/n[2])
print(s1*s2)
