# from flask_pymongo import PyMongo
from pymongo import MongoClient


# Setup MongoDB here
# mongo = PyMongo(uri="mongodb://localhost:27017/database")

mongo = MongoClient('mongodb://localhost:27017/')
db = mongo['webhook_db']
db.drop_collection("events")
collection = db['events']