k = 0
sum_out = 163
sum_in = 88
print('outgoing = %d' % sum_out)
print('incoming = %d' % sum_in)

sumI = float((sum_out / (sum_out + sum_in)) * 100)
sumY = float((sum_in / (sum_out + sum_in)) * 100)
print('percentage of outgoing calls = ',end='')
print(sumI)
print('percentage of incoming calls = ',end='')
print(sumY)
