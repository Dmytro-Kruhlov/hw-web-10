from pymongo import MongoClient


def get_mongodb():
    client = MongoClient("mongodb+srv://hazzy:hazzy1990@cluster0.s9aqskd.mongodb.net/")
    
    db = client.hw10
    return db
