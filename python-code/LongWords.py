def LongWords(word):
    if len(word) > 10:
        word = word[0] + str(len(word[1:len(word)-1])) + word[len(word)-1]
    return word

n = int(input(''))
a = ''
for i in range(0,n):
    a = a + str(LongWords(input(''))) + '\n'
print(a)
