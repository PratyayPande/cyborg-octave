def strRot(s,first,last):
    s = s[0:first] + s[last] + s[first+1:len(s)]
    return s


