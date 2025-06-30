from flask import Flask
from flask_restful import Api

from routes.catalog import ProductList

app = Flask(__name__)                                           
api = Api(app)

api.add_resource(ProductList, '/catalog')

if __name__ == '__main__':
    app.run(debug=True)