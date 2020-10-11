import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import JWT,jwt_required
from security import authenticate, identity
from models.item import ItemModel

        
class ItemList(Resource):
    def get(self):
        return {"items":[item.json() for item in ItemModel.query.all()]}
