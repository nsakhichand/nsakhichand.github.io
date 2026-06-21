from pymongo import MongoClient
from pymongo.errors import PyMongoError

class CRUD:
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:27017/aac?authSource=admin' % (username, password))
        self.database = self.client['aac']
        self.collection = self.database['animals']

    def create(self, data):
        
        if data is not None:
            try:
                result = self.collection.insert_one(data)
                return result.inserted_id is not None
            except PyMongoError as e:
                print(f"An error occurred while inserting data: {e}")
                return False
        else:
            raise ValueError("Data parameter is empty")

    def read(self, criteria=None):

        try:
            if criteria is not None:
                cursor = self.collection.find(criteria, {"_id": False})
            else:
                cursor = self.collection.find({}, {"_id": False})
            
            # Convert cursor to list for returning
            return list(cursor)
        except PyMongoError as e:
            print(f"An error occurred while reading data: {e}")
            return []

    def update(self, initial, change):
        
        if initial is not None:
            try:
                if self.collection.count_documents(initial, limit=1) != 0:
                    update_result = self.collection.update_many(initial, {"$set": change})
                    return update_result.raw_result
                else:
                    return {"result": "No document was found"}
            except PyMongoError as e:
                print(f"An error occurred while updating data: {e}")
                return {"result": "Error during update"}
        else:
            raise ValueError("Initial criteria parameter is empty")

    def delete(self, remove):

        if remove is not None:
            try:
                if self.collection.count_documents(remove, limit=1) != 0:
                    delete_result = self.collection.delete_many(remove)
                    return delete_result.raw_result
                else:
                    return {"result": "No document was found"}
            except PyMongoError as e:
                print(f"An error occurred while deleting data: {e}")
                return {"result": "Error during delete"}
        else:
            raise ValueError("Remove criteria parameter is empty")
