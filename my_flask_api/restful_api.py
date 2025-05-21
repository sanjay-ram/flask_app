from flask import Flask, jsonify, request
from flask_restful import  Api

app = Flask(__name__)
api = Api(app)

to_do_list = []
id_counter = 0
@app.route('/to_do_list', methods=['GET'])
def get_to_do_list():
    return jsonify(to_do_list)

@app.route('/to_do_list', methods=['Post'])
def add_todo():
    global id_counter
    data = request.get_json()
    todo = {
        "id": id_counter,
        "title" : data['title'],
        "completed" : data['completed']
    }
    to_do_list.append(todo)
    id_counter += 1
    return jsonify(to_do_list), 201

@app.route('/to_do_list/<int:todo_id>', methods=['Get'])
def get_todo(todo_id):
    if todo_id < len(to_do_list):
        return jsonify(to_do_list[todo_id]), 200
    return jsonify({'error': 'Item not found'}), 404

@app.route('/to_do_list/<int:todo_id>', methods=['PUT'])
def put_todos(todo_id):
    if todo_id < len(to_do_list):
        data = request.get_json()
        to_do_list[todo_id] = data
        return jsonify(to_do_list), 200
    return jsonify({'error': 'Todo not found'}), 404

@app.route('/to_do_list/<int:todo_id>', methods=['DELETE'])
def delete_todos(todo_id):
    global to_do_list
    if todo_id < len(to_do_list):
        to_do_list.pop(todo_id)
        return jsonify({'message': 'Todo deleted'}), 200
    return jsonify({'error': 'Todo not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)