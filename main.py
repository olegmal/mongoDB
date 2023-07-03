from pymongo import MongoClient
import json


client = MongoClient("mongodb://localhost:27017/")
db = client["test_hillel_db"]

collection = db["my_collection"]

kaspar = {"name": "Kaspar", "emai": "knaden1@jiathis.com"}
test_user1 = {"name":"test_name1", "email": "test_mail1@gmail.com"}
test_user2 = {"name": "test_name2", "email": "test_mail2@gmail.com"}

# collection.insert_many([test_user1, test_user2])
collection.update_many({}, {"$set": {"age":33}})

items = collection.find()
print(items)
for item in items:
    if item["name"] == "test_name_1":
        collection.delete_one(item)
    print(item)


