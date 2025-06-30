from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import models

app = Flask(__name__)
api = Api(app)

class UserList(Resource):
    def get(self):
        return jsonify([{'id': row[0], 'product_name': row[1], 'descrip': row[2], 'img_path': row[3], 'price': row[4], 'product_number': row[5]} for row in models.get_all_products()])
    
    def post(self):
        