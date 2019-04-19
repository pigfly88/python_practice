books = {'title':'php', 'author':'', 'price':9.9}
print(books['title'])

for k,v in books.items():
    print(k + " - " + str(v))

for v in books.values():
    print(v)

for k in books.keys():
    print(k)

for k,v in sorted(books.items()):
    print(k + " - " + str(v))

books = [
    {'title':'php', 'price':9.9},
    {'title':'java', 'price':11.09}
]
for book in books:
    print(book['title'])