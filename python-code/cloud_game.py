def jumpingOnClouds(c):
    leaps = 0
    if len(c) >= 3:
        skip = 1
        leaps = 1
        if c[2] == 0:
            skip = 2
        leaps += jumpingOnClouds(c[skip:])
    if len(c) == 2:
        leaps = 1
    return leaps


print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))
