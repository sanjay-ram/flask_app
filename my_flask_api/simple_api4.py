from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

products = {}
id_product = 0

class Product(Resource):
    def post(self):
        global id_product
        data = request.get_json()
        product = {
            "price": data["price"]
        }
        id_product += 1
        products.update(product)
        return jsonify(products), 201

    def put(self):
        global id_product
        if id_product < len(products):
            product = request.get_json()
            products[id_product] = product
            return jsonify(product), 200
        return {'error' : 'Product not found'}, 404

    def get(self):
        return jsonify(products), 200
    def delete(self):
        global id_product
        if id_product < len(products):
            products.pop(id_product)
            return {'message' : 'Product deleted'}, 201
        return {'error' : 'Product not found'}, 404

api.add_resource(Product, '/product/<name>')
if __name__ == '__main__':
    app.run(debug=True)