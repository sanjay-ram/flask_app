from flask import Flask, jsonify, request
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)

users = []

class User(Resource):
    def post(self):
        data = request.get_json()
        if not data or 'name' not in data:
            return {'message': 'Name required'}, 400
        users.append(data['name'])
        return {'message': 'User created'}, 201
    def get(self):
        return jsonify({'users': users})

api.add_resource(User, '/users')
if __name__ == '__main__':
    app.run(debug=True)