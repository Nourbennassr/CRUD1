from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

# Configuration de la base de données MongoDB
app.config['MONGO_URI'] = 'mongodb://localhost:27017/users'
mongo = PyMongo(app)

from app.views import user_view

if __name__ == '__main__':
    app.run()

