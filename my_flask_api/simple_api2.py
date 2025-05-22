from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class User(Resource):
    def get(self, name):
        return jsonify({'name' : name})

api.add_resource(User, '/user/<string:name>')
if __name__ == '__main__':
    app.run(debug=True)