from flask import Flask, request
from flask_restful import Resource, Api, abort
app = Flask(__name__)
api = Api(app)
contacts = []
current_id = 0
def get_contact_or_abort(contact_id):
    for contact in contacts:
        if contact['id'] == contact_id:
            return contact
    abort(404, message=f"Contact with id {contact_id} not found")

class Contact(Resource):
    def get(self, contact_id):
        contact = get_contact_or_abort(contact_id)
        return contact, 200
    def put(self, contact_id):
        contact = get_contact_or_abort(contact_id)
        data = request.get_json(force=True)
        name = data.get("name")
        phone = data.get("phone")
        if not name or not phone:
            abort(400, message="Name and phone are required")
        contact['name'] = name
        contact['phone'] = phone
        return contact, 200
    def delete(self, contact_id):
        global contacts
        contact = get_contact_or_abort(contact_id)
        contacts = [c for c in contacts if c ['id'] != contact_id]
        return {'message': f'Contact with id {contact_id} deleted'}, 200

class ContactsList(Resource):
    def get(self):
        name_filter = request.args.get("name")
        if name_filter:
            filtered = [c for c in contacts if name_filter.lower() in c ['name'].lower()]
            return filtered, 200
        return contacts, 200

    def post(self):
        global current_id
        data = request.get_json(force=True)
        name = data.get("name")
        phone = data.get("phone")
        if not name or not phone:
            abort(400, message="Name and phone are required")
        current_id += 1
        contact = {
            'id': current_id,
            'name': name,
            'phone': phone
        }
        contacts.append(contact)
        return contact, 201

api.add_resource(ContactsList, '/contacts')
api.add_resource(Contact, '/contacts/<int:contact_id>')

if __name__ == '__main__':
    app.run(debug=True)