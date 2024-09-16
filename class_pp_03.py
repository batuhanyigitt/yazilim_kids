words = ['data', 'science', 'machine', 'learning']
word_length = []
for word in words:
    word_length.append(len(word))
print(word_length)


words = ['data', 'science', 'machine', 'learning']
word_length = list(map(lambda item: len(item), words))
print(word_length)


words = ['data', 'science', 'machine', 'learning']
word_length = [len(word) for word in words]
print(word_length)



L1 = [
    ('Bread', 10),
    ('Butter', 20),
    ('Chocolate dark', 15),
    ('Chocolate milk', 17),
    ('Cakes', 19)
]

product_prices = [item[1]*1.2 for item in L1]
print(product_prices)


L1 = [
    ('Bread', 10),
    ('Butter', 20),
    ('Chocolate dark', 15),
    ('Chocolate milk', 17),
    ('Cakes', 19)
]

prices = [item[1]*1.2 for item in L1 if item[1] >= 15]
print(prices)



words = ['data', 'science', 'machine', 'learning']
word_length = {}
for word in words:
    word_length[word] = len(word)
    print(word_length)
    
    
shaskespeare = 'When forty winters shall besiege thy brow, And dig deep trenches in thy beautys field, ...'
shaskespeare = shaskespeare.replace(',', '').replace('.', '')
words = shaskespeare.split()
word_length = ()
for word in words:
    word_length[word] = len(word)
    print(word_length)
    


words = ['data', 'science', 'machine', 'learning']
word_length = {word: len(word) for word in words}
print(word_length) 
   
   
   
shaskespeare = 'When forty winters shall besiege thy brow, And dig deep trenches in thy beautys field, ...'
words  = shaskespeare.replace(',', '').replace('.', '').split()
word_length = {word: len(word) for word in words}
print(word_length)


product_prices_dic = [
    ('Bread', 10),
    ('Butter', 20),
    ('Chocolate dark', 15),
    ('Chocolate milk', 17),
    ('Cakes', 19)
]

product_prices_increased = {k: v*1.2 for k, v in product_prices_dic.items()}
print(product_prices_increased)