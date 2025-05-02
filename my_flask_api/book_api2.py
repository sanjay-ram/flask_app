from flask import Flask
from flask_restful import Api
from book import db
from book_api import Books

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Data7Dollar$@localhost:3306/bookstore'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

api = Api(app)
api.add_resource(Books, '/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
