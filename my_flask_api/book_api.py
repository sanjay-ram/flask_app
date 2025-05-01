from flask import Flask, request
from flask_restful import Api, Resource
from inserting_books import insert_book
import json
app = Flask(__name__)
api = Api(app)

class Books(Resource):

    def get(self):
        with open('books.json') as books_file:
            books = json.load(books_file)
        return books, 200
    def post(self):
        data = request.get_json()
        title = data.get('title')
        author = data.get('author')
        return insert_book(title, author)


    def put(self):
        data = request.get_json()
        title = data.get('title')
        author = data.get('author')
        return insert_book(title, author)

api.add_resource(Books, '/books')
if __name__ == '__main__':
    app.run(debug=True)