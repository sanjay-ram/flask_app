from flask import Flask, jsonify, request
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


books = []

@app.route('/books', methods=['POST'])
def add_book():
    book_data = request.get_json()
    if not all(key in book_data for key in ('title', 'author', 'publishing_year')):
        return jsonify({'error': 'Missing data'}), 400

    book_id = len(books)  
    book = {
        'id': book_id,
        'title': book_data['title'],
        'author': book_data['author'],
        'publishing_year': book_data['publishing_year']
    }
    books.append(book)
    return jsonify(book), 201


@app.route('/books', methods=['Get'])
def get_books():
    return jsonify(books), 200

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    if book_id < len(books):
        book = request.get_json()
        books[book_id] = book
        return jsonify(book), 200
    return jsonify({'error': 'Book  not found'}), 404




if __name__ == '__main__':
    app.run(debug=True)