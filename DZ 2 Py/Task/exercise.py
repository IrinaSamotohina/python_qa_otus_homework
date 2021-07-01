import json
from csv import DictReader


with open('books.csv', 'r') as b:
    reader = DictReader(b)
    a = list(reader)
    for row in a:
        books = json.dumps(a, indent=4)
        with open('books.json', 'w') as book:
            book.write(books)


with open('user.json', 'r') as user_data:
    with open('books.json', 'r') as book_data:
        users_reader = json.loads(user_data.read())
        books_reader = json.loads(book_data.read())
        while len(books_reader) != 0:
            res = []
            for u in users_reader:
                if len(books_reader) == 0:
                    break
                q = books_reader[0]
                if u.get('books') is None:
                    a = {'books': [q]}
                    u.update(a)
                else:
                    d = u.get('books')
                    d.append(q)
                books_reader.remove(q)

        for u in users_reader:
            res.append({
                'index': u.get('index'),
                'name': u.get('name'),
                'age': u.get('age'),
                'gender': u.get('gender'),
                'address': u.get('address'),
                'books': u.get('books')
            })


with open('result.json', 'w') as data:
    data_all = json.dumps(res, sort_keys=False, indent=2)
    data.write(data_all)