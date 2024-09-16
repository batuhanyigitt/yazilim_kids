if re.search('[a-zA-Z]ana\Z[aA]', sys.argv[1]):
    print('a match')
else:
    print('no match')
    
    
if re.search(r"he*o", sys.argv[1]):
    print('a match')
else:
    print('no match')
    

if re.search('[b-e]a$', sys.argv[1]):
    print('a match')
else:
    print('no match')
    
    
txt = "This is banana. Banana is very good."
l1 = re.findall('banana', txt)
print(L1)