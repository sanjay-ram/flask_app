import csv
from book import db, app  # import app too!
from book import Book

def insert_books(csv_file_name):
    with open(csv_file_name, newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            book = Book(
                id=int(row['id']),
                title=row['title'],
                author=row['author']
            )
            db.session.add(book)
        db.session.commit()
    print("Books inserted successfully")
def insert_book(title, author):
    '''
    todo: vor dem Abspeichern auf die Datenbank, überprüfen ob
    das Buch bereits existiert oder nicht.
    :param title:
    :param author:
    :return:
    '''
    existing_book = Book.query.filter_by(title=title, author = author).first()
    if existing_book:
        return {"message": "Book already exists."}, 409
    else:
        new_book = Book(title=title, author=author)
        db.session.add(new_book)
        db.session.commit()
        return {"message": "Book inserted successfully."}, 201
if __name__ == '__main__':
    with app.app_context():  # ✅ This fixes your issue
        insert_books('books.csv')
