import numpy as np

def createHash(st):



k = int(input('Enter the number of test cases: '))
for i in range(0,k):
    ln = int(input('Enter the length of the strings: '))
    str1 = input('Enter the first string: ')
    str2 = input('Enter the second string: ')
    nm = list(range(0,ln))
    dict1 = dict(zip())
    if (len(str1) == len(str2)):

