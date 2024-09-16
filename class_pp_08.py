sentence = sys.argv[1]
print(len(sentence))


L1 = sys.argv
print(L1)

n1 = sys.argv[1]
n2 = sys.argv[2]


print(n1*n2)



vowels = 'aeiou'
word = 'Winnepesaukee'

vowelcount = 0 

for letter in word:
    if letter in vowels:
        vowelcount += 1
print(f'There are {vowelcount} vowels in {word}')




vowels = 'aeiou'
words= sys.argv[1:]

word_no = 0 

for word in words:
    vowelcount = 0
    word_no += 1 
    for letter in word:
        if letter in vowels:
        vowelcount += 1
print(f'There are {vowelcount} vowels in {word_no}')



sample_file = open('sample.txt', 'r')

inFile = open('testfile.txt', 'r', encoding='utf-8')
stuff = inFile.read()
inFile.close()
print(stuff)


outFile = open('testfile.txt', 'w', encoding='utf-8')
outFile.write('This is a test file')
outFile.write('... and some more text\n')
outFile.close()
