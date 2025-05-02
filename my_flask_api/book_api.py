from flask import Flask
from flask_restful import Api, Resource, reqparse
from book import Book, db
app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('title', required=True)
parser.add_argument('author', required=True)

class Books(Resource):
    def get(self):
        books = Book.query.all()
        return {'books': [book.to_dict() for book in books]}, 200

    def post(self):
        args = parser.parse_args()
        title, author = args['title'], args['author']
        existing = Book.query.filter_by(title=title, author=author).first()
        if existing:
            return {"message": "Book already exists."}, 409
        new_book = Book(title=title, author=author)
        db.session.add(new_book)
        db.session.commit()
        return {"message": "Book inserted successfully."}, 201

