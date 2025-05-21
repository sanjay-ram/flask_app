from flask import Flask, request, jsonify
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

users = []

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = {
        'id' : data['id'],
        'username': data['username'],
        'email': data['email'],
        'password': data['password']
    }
    users.append(user)
    return jsonify(user), 201
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id < len(users):
        return jsonify(users[user_id]), 200
    return jsonify({'error': 'User  not found'}), 404




if __name__ == '__main__':
    app.run(debug=True)