from bson import ObjectId
from app import mongo

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def save(self):
        mongo.db.users.insert_one({
            'username': self.username,
            'email': self.email
        })

    @staticmethod
    def get_all():
        return mongo.db.users.find()

    @staticmethod
    def get_by_id(user_id):
        user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
        return user

    def update(self, user_id):
        mongo.db.users.update_one({'_id':ObjectId(user_id)}, {'$set': {
            'username': self.username,
            'email': self.email
        }})

    @staticmethod
    def delete(user_id):
     mongo.db.users.delete_one({'_id': ObjectId(user_id)})
   