egg_path='mf2.egg'

import sys
sys.path.append(egg_path)
from morfeusz2 import *
from flask import Flask
from flask_restful import Resource, Api
reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class CaseTagger(Resource):
    def get(self, text):
        return analyse(text)

api.add_resource(HelloWorld, '/')
api.add_resource(CaseTagger, '/casetags/<string:text>')

if __name__ == '__main__':
    app.run(debug=True)
