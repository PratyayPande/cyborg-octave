import math
import matplotlib

def nonDivisibleSubset(k, s):
    # Write your code here
    largest_size = 0
    set_size = len(s)
    pow_set_size = int(math.pow(2, set_size))
    # declare array to store all permutations
    perm = []
    # Run from counter 000..01 to 111..10
    for counter in range(pow_set_size, 0, -1):
        nm = []
        # finding the permutations
        for j in range(0, set_size):
            if (counter & (1 << j)) > 0:
                nm.append(s[j])
        # found one premutation
        # now check if the sun of any 2 elements of nums is divisible by k
        perm.append(nm)
        ncount = len(nm)
        b = True
        for i in range(0, ncount - 1):
            for j in range(i + 1, ncount):
                if (nm[i] + nm[j]) % k == 0 or nm[i] == nm[j]:
                    b = False
                    break
            if not b:
                break
        if b and ncount > largest_size:
            largest_size = ncount
    return largest_size




# d = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
d = [2, 7, 12, 17, 22]
f = 5
print(nonDivisibleSubset(f, d))
