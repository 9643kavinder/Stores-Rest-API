from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT,jwt_required
from security import authenticate, identity
from models.users import UserModel
from models.item import ItemModel
from models.stores import StoreModel
from resources.item import Item, ItemList
from resources.users import UserRegister
from resources.stores import Store, StoreList
from db import db
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "kavinder"
api = Api(app)
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()


jwt = JWT(app, authenticate, identity)      ### /auth
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister,'/register')




if __name__ == '__main__':
    app.run(port=5000, debug=True)
