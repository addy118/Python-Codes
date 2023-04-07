books = ['novel', 'novella', 'erotica', 'poetry']
print(books)
print(books[:])
# 0:len(books)-1
print(books[1:-3])
# len(books)-3 =4-3 =1
# null
print(books[1:-2])
# 1:2
print(books[2:3])

if 'novel' in books:
    print('Yes')
else:
    print('No')

if 'noval' in books:
    print('Yes')
else:
    print('No')

book = ['fiction', books]
print(book)

for i in books:
    print(i)