from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class greeting(Resource):
    def get(self):
        return {'greeting': 'Hello Welt!'}


api.add_resource(greeting, '/')
if __name__ == '__main__':
    app.run(debug=True)