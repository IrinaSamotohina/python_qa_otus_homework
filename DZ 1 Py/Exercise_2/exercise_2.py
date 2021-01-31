import json
from csv import DictReader


with open('books.csv', 'r') as b:
    reader = DictReader(b)
    a = list(reader)
    for row in a:
        books = json.dumps(a, indent=4)
        with open('../Exercise_1/books.json', 'w') as book:
            book.write(books)


with open('user.json', 'r') as user_data:
    with open('../Exercise_1/books.json', 'r') as book_data:
        users_reader = json.loads(user_data.read())
        books_reader = json.loads(book_data.read())
        res = []
        for u in users_reader:
            q = books_reader[0]
            res.append(
                {
                    "name": u["name"],
                    'gender': u["gender"],
                    'address': u["address"],
                    'books': [
                        {
                            'Title': q["Title"],
                            'Author': q["Author"],
                            'Height': q["Height"]
                        }]
                }
            )
            books_reader.remove(q)


with open('books_and_users.json', 'w') as data:
    data_all = json.dumps(res, sort_keys=False, indent=2)
    data.write(data_all)