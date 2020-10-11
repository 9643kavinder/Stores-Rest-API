from flask_restful import Resource
from models.stores import StoreModel

class Store(Resource):
    def get(self,name):
        store = StoreModel.get_item(name)
        if store:
            return store.json()
        return {'message' : 'store not found'},404
    
    def post(self,name):
        if StoreModel.get_item(name):
            return {'mesage' : 'A store with {} already exists'.format(name)},400
        store  = StoreModel(name)
        try:
            store.save_to_db()
        except:
            {'message' : 'An errr occured while creating the store.'},500

        return store.json()

    def delete(self,name):
        store = StoreModel.get_item(name)
        if store:
            store.delete_from_db()
        return {'message' : 'store deleted'}


class StoreList(Resource):
    def get(self):
        return {'stores':[store.json() for store in StoreModel.query.all()]}