from pymongo import MongoClient
from pymongo.errors import PyMongoError

class CRUD:
    """ 
    Enhanced CRUD operations for Animal collection in MongoDB 
    - Improved for CS 499 Milestone Two (Software Design & Engineering)
    - Added better docstrings and comments for maintainability
    """

    def __init__(self, username, password):
        """Initialize MongoDB connection"""
        self.client = MongoClient(f'mongodb://{username}:{password}@localhost:27017/aac?authSource=admin')
        self.database = self.client['aac']
        self.collection = self.database['animals']
        print("✅ Connected to MongoDB - Grazioso Salvare Animals Collection")

    def create(self, data):
        """Create a new animal document"""
        if data is None:
            raise ValueError("Data parameter is empty")
        try:
            result = self.collection.insert_one(data)
            return result.inserted_id is not None
        except PyMongoError as e:
            print(f"❌ Create error: {e}")
            return False

    def read(self, criteria=None):
        """Read animals with optional filter"""
        try:
            if criteria:
                cursor = self.collection.find(criteria, {"_id": False})
            else:
                cursor = self.collection.find({}, {"_id": False})
            return list(cursor)
        except PyMongoError as e:
            print(f"❌ Read error: {e}")
            return []

    def update(self, initial, change):
        """Update animals matching criteria"""
        if initial is None:
            raise ValueError("Initial criteria parameter is empty")
        try:
            if self.collection.count_documents(initial, limit=1) > 0:
                result = self.collection.update_many(initial, {"$set": change})
                return result.raw_result
            return {"result": "No document was found"}
        except PyMongoError as e:
            print(f"❌ Update error: {e}")
            return {"result": "Error during update"}

    def delete(self, remove):
        """Delete animals matching criteria"""
        if remove is None:
            raise ValueError("Remove criteria parameter is empty")
        try:
            if self.collection.count_documents(remove, limit=1) > 0:
                result = self.collection.delete_many(remove)
                return result.raw_result
            return {"result": "No document was found"}
        except PyMongoError as e:
            print(f"❌ Delete error: {e}")
            return {"result": "Error during delete"}