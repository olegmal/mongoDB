from pymongo import MongoClient
import json


client = MongoClient("mongodb://localhost:27017/")
db = client["test_hillel_db"]

collection = db['garden_staff']

class GardenStaff:
    def __int__(self, vegetables: str, fruits: str, price: float):
        self.vegetables: str = vegetables
        self.fruits: str = fruits
        self.price: float = price

class Person:
    def __int__(self, _id: str, name: str, email: str, phone: str, garden_stuff: list):
        self._id = _id
        self.name: str = name
        self.email: str = email
        self.phone: str = phone
        self.garden_stuff: list[GardenStaff] = garden_stuff

    def __str__(self):
        return f"{self._id} {self.name} {self.email} {self.phone} {len(self.garden_stuff)}"

def convert_person_to_object(base_dict: dict) -> Person:
    list_of_goods = base_dict["garden_stuff"]
    goods_list = list()
    for product in list_of_goods:
        vegetables_in_list = GardenStaff(product["vegetables"], product["price"])
        fruits_in_list = GardenStaff(product["fruits"], product["price"])
        goods_list.append(vegetables_in_list)
        goods_list.append(fruits_in_list)
    result_person = Person(base_dict["_id"], base_dict["name"], base_dict["email"], base_dict["phone"], goods_list)
    return result_person


with open('garden_staff.json') as file:
    file_data = json.load(file)

collection.insert_many(file_data)
person_for_moving_to_object = collection.find_one({"name": "Charles"})
print(person_for_moving_to_object)
print(convert_person_to_object(person_for_moving_to_object))
