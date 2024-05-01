from flask import Flask
from flask_restful import Resource, Api,reqparse

app = Flask(__name__)
api = Api(app)

parser=reqparse.RequestParser(trim=False,bundle_errors=True)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)