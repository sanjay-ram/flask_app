from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
products = {}

class Products(Resource):
    def get(self, name):
        if name in products:
            return jsonify({name : products[name]}), 200
        return {'message': 'Product not found'}, 404




api.add_resource(Products, '/products/Unbekannt')
if __name__ == '__main__':
    app.run(debug=True)
