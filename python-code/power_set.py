import math
import numpy as np
import math as mt

def powerset(the_set):
    # set_size of power set of a set
    # with set_size n is (2**n -1)
    set_size = len(the_set)
    pow_set_size = int(math.pow(2, set_size))
    # Run from counter 000..0 to 111..1
    for counter in range(pow_set_size-1,0,-1):
        for j in range(0, set_size):

            # Check if jth bit in the
            # counter is set If set then
            # print jth element from set
            if (counter & (1 << j)) > 0:
                print(the_set[j], end="")
        print("")

    # Driver program


st = [1,2,3]
powerset(st)
