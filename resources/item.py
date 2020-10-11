from flask_restful import Resource, reqparse
from flask_jwt import JWT,jwt_required
from security import authenticate, identity
from models.item import ItemModel
import sqlite3
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required = True,
        help = "This field cannot be blank."
    )
    parser.add_argument('store_id',
        type = int,
        required = True,
        help = "Every item should have a store id."
    )

    @jwt_required()
    def get(self,name):
        item = ItemModel.get_item(name)
        if item:
            return item.json()
        return {"message":"Item not found."}
    
    def post(self,name):
        row = ItemModel.get_item(name)
        if row:
            return {"message" : "An item with name '{}' is already exist.".format(name)},400
        data = Item.parser.parse_args()
        item = ItemModel(name,data['price'],data['store_id'])
        item.save_to_db()
        return {"message" : "Item Added Successfully."},201
        

    def delete(self,name):
        item = ItemModel.get_item(name)
        if item:
            item.delete_from_db()
        return {"message" : "Item deleted successfully."}

    def put(self,name):
        item = ItemModel.get_item(name)
        data = Item.parser.parse_args()
        if item:
            item.price = data['price']
        else:
            item = ItemModel(name,data['price'],data['store_id'])
        item.save_to_db()
        return {"message" : "Item added successfully"}
    

class ItemList(Resource):
    def get(self):
        return {"items":[item.json() for item in ItemModel.query.all()]}